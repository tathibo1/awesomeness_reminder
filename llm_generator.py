import re
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

def remove_think_tags(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

def generate_message(prompt):
    llm = OllamaLLM(model="deepseek-r1:8b")
    response = llm.invoke(prompt)
    return remove_think_tags(response)