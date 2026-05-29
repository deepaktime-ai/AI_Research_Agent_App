from llm.llm import generate_response
from tools.web_search import web_search
from tools.rag_tool import rag_query


def execute_step(step):
    step_lower = step.lower()

    # 🔥 RAG trigger
    if "pdf" in step_lower or "document" in step_lower or "notes" in step_lower:
        return rag_query(step)

    # 🔥 Web search trigger
    if "search" in step_lower or "latest" in step_lower:
        return web_search(step)

    # Default LLM
    prompt = f"""
You are an AI research assistant.

Execute this step and give a detailed result:

Step: {step}
"""

    return generate_response(prompt)



