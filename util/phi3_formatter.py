import json
from langchain_core.outputs import Generation
from typing import (
    Dict,
    List
)
from langchain_community.llms.azureml_endpoint import (
    AzureMLEndpointApiType,
    ContentFormatterBase,
)


class CustomPhi3ContentFormatter(ContentFormatterBase):
    """Content formatter for models that use the OpenAI like API scheme."""

    @property
    def supported_api_types(self) -> List[AzureMLEndpointApiType]:
        return [AzureMLEndpointApiType.serverless]

    def format_request_payload(  # type: ignore[override]
        self, prompt: str, model_kwargs: Dict, api_type: AzureMLEndpointApiType
    ) -> bytes:
        """Formats the request according to the chosen api"""
        prompt = ContentFormatterBase.escape_special_characters(prompt)
        if api_type in [
            AzureMLEndpointApiType.serverless
        ]:
            request_payload = json.dumps(
                {
                    "messages": [
                        {"role": "user", "content": f'"{prompt}"'}
                    ]
                }
            )

        else:
            raise ValueError(
                f"`api_type` {api_type} is not supported by this formatter"
            )
        return str.encode(request_payload)

    def format_response_payload(  # type: ignore[override]
        self, output: bytes, api_type: AzureMLEndpointApiType
    ) -> Generation:
        """Formats response"""
        if api_type in [
            AzureMLEndpointApiType.serverless
        ]:
            try:
                choice = json.loads(output.decode('UTF-8'))["choices"][0]['message']['content']
            except (KeyError, IndexError, TypeError) as e:
                raise ValueError(self.format_error_msg.format(api_type=api_type)) from e  # type: ignore[union-attr]
            return Generation(text=choice)
        
        raise ValueError(f"`api_type` {api_type} is not supported by this formatter")

