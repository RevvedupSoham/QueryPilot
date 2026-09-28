import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    model = os.getenv("GROQ_MODEL")
    if not model:
        raise ValueError("GROQ_MODEL is not configured in .env.")
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY is not configured in .env.")
    return ChatGroq(model=model, temperature=0)
