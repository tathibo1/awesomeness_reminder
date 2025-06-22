import os
from langchain_anthropic import ChatAnthropic
from .base import LLMProvider

class AnthropicProvider(LLMProvider):
    def __init__(self):
        self.llm = ChatAnthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            model_name=os.getenv("ANTHROPIC_MODEL", "claude-3-sonnet-20240229")
        )
    
    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content