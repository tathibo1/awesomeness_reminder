import os
import re
from langchain_ollama import OllamaLLM
from llms.base import LLMProvider

class OllamaProvider(LLMProvider):
    def __init__(self):
        self.llm = OllamaLLM(model=os.getenv("OLLAMA_MODEL", "deepseek-r1:8b"))
    
    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()