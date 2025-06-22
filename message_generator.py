import os
from dotenv import load_dotenv
from llms.base import LLMProvider
from llms.anthropic import AnthropicProvider
from llms.local.ollama import OllamaProvider

load_dotenv()

def get_llm_provider() -> LLMProvider:
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    if provider == "ollama":
        return OllamaProvider()
    elif provider == "anthropic":
        return AnthropicProvider()
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

def generate_message(prompt):
    provider = get_llm_provider()
    response = provider.generate(prompt)
    print(f"Generated Message: {response}") 
    return response