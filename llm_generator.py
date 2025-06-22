import os
import re
from langchain_ollama import OllamaLLM
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

def remove_think_tags(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

def generate_message(prompt):
    response = "You're Grrrrrrrrreat!"
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    
    if provider == "ollama":
        model = os.getenv("OLLAMA_MODEL", "deepseek-r1:8b")
        llm = OllamaLLM(model=model)
        response = remove_think_tags(llm.invoke(prompt))
 
    elif provider == "anthropic":
        llm = ChatAnthropic(
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            model_name=os.getenv("ANTHROPIC_MODEL", "claude-3-sonnet-20240229")
        )
        response = llm.invoke(prompt).content

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
    
    return response
