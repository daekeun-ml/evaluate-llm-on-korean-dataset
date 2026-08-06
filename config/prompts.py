"""Prompt templates configuration"""

import os
from dotenv import load_dotenv

load_dotenv()


def _get_choice_letters(num_choices):
    """Get choice letters based on number of choices"""
    return ', '.join(chr(65 + i) for i in range(num_choices - 1)) + f', or {chr(65 + num_choices - 1)}'


def _get_choice_examples(num_choices):
    """Get example letters"""
    examples = ['A', chr(65 + num_choices // 2), chr(65 + num_choices - 1)]
    return '\n'.join(examples[:3])


def _generate_direct_prompt(num_choices):
    """Generate direct answer prompt"""
    return f"""CRITICAL: You MUST respond with EXACTLY ONE LETTER ONLY ({_get_choice_letters(num_choices)}).

ABSOLUTELY NO explanations, reasoning, or additional text.

Just the letter. Period.

Examples of CORRECT responses:
{_get_choice_examples(num_choices)}

Examples of WRONG responses (NEVER do this):
- "A. The answer is..."
- "I think the answer is C"
- "C\\n\\nBecause..."
- "Answer: B"
- "The correct choice is D"

RESPOND WITH ONLY ONE LETTER."""


def _generate_reasoning_prompt(num_choices, reasoning_effort="medium"):
    """Generate reasoning prompt based on effort level"""
    effort_instructions = {
        "none": "Keep your reasoning VERY BRIEF (1 sentence maximum)",
        "minimal": "Keep your reasoning BRIEF (1-2 sentences maximum)",
        "low": "Keep your reasoning CONCISE (2-3 sentences maximum)",
        "medium": "Provide clear reasoning (3-4 sentences maximum)",
        "high": "Provide detailed reasoning and analysis (4-6 sentences maximum)",
        # Self-hosted DeepSeek-V4-Flash exposes a "max" level; without an entry here it
        # silently fell back to "medium". Note that asking for brevity does NOT actually
        # bound this model's reasoning: its own effort prompt (injected by the checkpoint's
        # encoder) tells it to keep verifying until certain, and that wins. Truncation is
        # handled at the decoding layer instead — see util/forced_close_llm.py.
        "max": "Provide thorough reasoning, but keep it under 300 words. Do NOT enumerate every option exhaustively, and do NOT revisit conclusions you already reached — decide and commit",
    }
    
    instruction = effort_instructions.get(reasoning_effort, effort_instructions["medium"])
    
    return f"""You are a multiple-choice question answerer. Your task is to analyze the question carefully and select the single best answer.

INSTRUCTIONS:
1. {instruction}
2. After reasoning, provide your answer in the format: ### ANSWER followed by a single letter
3. Your answer must be ONLY one uppercase letter: {_get_choice_letters(num_choices)}

CORRECT OUTPUT FORMAT:
[Reasoning based on {reasoning_effort} effort level]

### ANSWER
A

INCORRECT OUTPUT EXAMPLES:
- "C"
- The answer is C
- C.
- Answer: C
- (C)
- [C]
- ```C```

Remember: Follow the {reasoning_effort} reasoning level and always use ### ANSWER format."""


def _is_reasoning_enabled():
    """Check if reasoning is enabled from environment variables"""
    return os.getenv("REASONING_ENABLED", "false").lower() == "true"


def get_system_prompt(num_choices=5):
    """Get system prompt based on number of choices and reasoning configuration
    
    Args:
        num_choices: Number of answer choices (4, 5, 10, etc.)
    """
    reasoning_enabled = _is_reasoning_enabled()
    reasoning_effort = os.getenv("REASONING_EFFORT", "medium")
    
    if reasoning_enabled:
        prompt = _generate_reasoning_prompt(num_choices, reasoning_effort)
        mode = f"Reasoning mode enabled ({reasoning_effort} effort)"
    else:
        prompt = _generate_direct_prompt(num_choices)
        mode = "Direct answer mode"
    
    print(f"[INFO] System Prompt - {mode} ({num_choices} choices)")
    
    return prompt


def get_math_system_prompt():
    """Get system prompt for math problems (HRM8K)"""
    prompt = """Your task is to solve the following math problem step by step.

INSTRUCTIONS:
1. Read the problem carefully
2. Show your step-by-step reasoning
3. Write your final answer in the format: ### ANSWER followed by only the numerical value

EXAMPLE:
Question: Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?

Solution:
Janet's ducks lay 16 eggs per day.
She eats 3 eggs for breakfast.
She uses 4 eggs for baking muffins.
So she has 16 - 3 - 4 = 9 eggs left to sell.
She sells each egg for $2.
Therefore, she makes 9 × $2 = $18 per day.

### ANSWER
18

Now solve the given problem following this format."""
    
    print(f"[INFO] System Prompt - Math problem solving mode")
    
    return prompt
