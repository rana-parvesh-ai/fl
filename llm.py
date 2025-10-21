# llm_agent.py
import json
from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

def ask_llm_direct(user_query, context_data):
    """
    context_data: list of JSON-serializable dicts
    """
    context_json = json.dumps(context_data, ensure_ascii=False, indent=2)
    prompt = f"""
You are a data analyst. Generate a MongoDB query to answer the user query using ONLY the following MongoDB data schema (JSON array):

{context_json}

Question: {user_query}
"""

    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role":"user","content":prompt}],
        max_tokens=512
    )
    # print(resp.choices[0].message.content)
    return resp.choices[0].message.content
