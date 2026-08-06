"""Forced-thinking-close LLM for self-hosted DeepSeek-V4-Flash.

Why this exists
---------------
DeepSeek-V4-Flash's `reasoning_effort` is not an API parameter — it is a prompt
prefix injected at the front of the conversation (see the model's
`encoding/encoding_dsv4.py`, `REASONING_EFFORT_PROMPTS`). The `max` level tells the
model "Do not stop reasoning until you have independently verified the solution
from multiple angles", so on hard multiple-choice items it never emits `</think>`
within any practical token budget: the whole budget goes to reasoning and the
response content comes back empty.

Measured on the first 30 KoBALT-700 items (max_tokens=8192, temperature=0.01):

    official max + forced close   80.0% acc, 24/30 self-closed, 3913 avg tokens
    time-boxed "under 400 words"  73.3% acc, 27/30 self-closed, 1841 avg tokens
    official low (baseline)       73.3% acc, 26/30 self-closed, 1928 avg tokens

Constraining the reasoning via the prompt does cut tokens roughly in half, but it
also drops accuracy back to the `low` baseline — i.e. a constrained `max` is just
an expensive `low`. Forcing the close keeps `max`-level accuracy instead.

So this class talks to the raw `/completions` endpoint (bypassing vLLM's
`deepseek_v4` reasoning parser, which discards reasoning text unless `</think>`
is actually emitted), and when the budget runs out mid-thought it appends
`</think>\n\n### ANSWER\n` and asks for just the letter. That converts what used
to be an empty response into a real answer grounded in the reasoning done so far.
"""

import os
import sys
from typing import Any, List, Optional

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

THINK_CLOSE = "</think>"
ANSWER_CUE = "\n</think>\n\n### ANSWER\n"

# Choice letters, so the forced answer can be constrained to a single token.
_CHOICE_LETTERS = [chr(65 + i) for i in range(10)]  # A-J


def _load_official_encoder():
    """Import the encoder shipped inside the model checkpoint.

    The prompt format uses full-width delimiters (`<｜User｜>`, not `<|User|>`) and a
    BOS token, so hand-rolling it silently produces a malformed prompt. Always use
    the checkpoint's own encoder.
    """
    encoding_dir = os.getenv(
        "DEEPSEEK_ENCODING_DIR",
        "/opt/dlami/nvme/models/DeepSeek-V4-Flash-0731/encoding",
    )
    if encoding_dir not in sys.path:
        sys.path.insert(0, encoding_dir)
    import encoding_dsv4  # noqa: PLC0415

    return encoding_dsv4


class ForcedCloseDeepSeekLLM(LLM):
    """DeepSeek-V4-Flash via raw /completions, force-closing an unfinished think block."""

    base_url: str = "http://localhost:8000/v1"
    api_key: str = "EMPTY"
    model: str = "deepseek-v4-flash"
    reasoning_effort: str = "max"
    system_prompt: Optional[str] = None
    max_tokens: int = 4096
    temperature: float = 0.01
    request_timeout: float = 1200.0
    answer_max_tokens: int = 8

    @property
    def _llm_type(self) -> str:
        return "forced_close_deepseek"

    def _client(self):
        import openai  # noqa: PLC0415

        return openai.OpenAI(
            base_url=self.base_url, api_key=self.api_key, timeout=self.request_timeout
        )

    def _build_prompt(self, question: str) -> str:
        enc = _load_official_encoder()

        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": question})

        # Encode with the neutral "low" level (which contributes no prefix), then
        # prepend the effort prompt ourselves so the level is explicit and visible.
        prompt = enc.encode_messages(
            messages, thinking_mode="thinking", reasoning_effort="low"
        )
        effort_prefix = enc.REASONING_EFFORT_PROMPTS[self.reasoning_effort]
        if not effort_prefix:
            return prompt

        bos = getattr(enc, "BOS_TOKEN", "<｜begin▁of▁sentence｜>")
        if prompt.startswith(bos):
            return bos + effort_prefix + prompt[len(bos) :]
        return effort_prefix + prompt

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        client = self._client()
        encoded = self._build_prompt(prompt)

        first = client.completions.create(
            model=self.model,
            prompt=encoded,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        text = first.choices[0].text

        if THINK_CLOSE in text:
            # Model finished thinking on its own; downstream parsers only want the
            # post-</think> content.
            return text.split(THINK_CLOSE, 1)[1]

        # Budget exhausted mid-thought. Close the block and ask for the letter only,
        # keeping the reasoning so far in context.
        forced = client.completions.create(
            model=self.model,
            prompt=encoded + text + ANSWER_CUE,
            max_tokens=self.answer_max_tokens,
            temperature=self.temperature,
        )
        answer = forced.choices[0].text

        # Occasionally the model starts explaining instead of emitting a letter, and the
        # tiny budget cuts it off before any letter appears (~0.2% of items). Retry once
        # with a blunter cue so the parser still gets something to read.
        if not any(letter in answer.upper() for letter in _CHOICE_LETTERS):
            retry = client.completions.create(
                model=self.model,
                prompt=(
                    encoded
                    + text
                    + "\n</think>\n\nOutput only the answer letter, nothing else.\n### ANSWER\n"
                ),
                max_tokens=4,
                temperature=self.temperature,
            )
            answer = retry.choices[0].text or answer

        return "### ANSWER\n" + answer
