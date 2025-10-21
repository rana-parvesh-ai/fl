# config.py
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://joc-dbuser:n5cqzIJSl319TZN6@mongo-airlineops-az-ddb01-pl-0.npznw.mongodb.net/")
MONGO_DB = os.getenv("MONGO_DB", "test_db")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
