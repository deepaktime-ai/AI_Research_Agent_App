from llm.llm import generate_response


def web_search(query):
    """
    Simulated web search using LLM (Phase 4 basic version)
    Later we will replace with real API (SerpAPI, Tavily, etc.)
    """

    prompt = f"""
You are a web search engine.

Search the internet and return factual, updated, and concise information.

Query: {query}
"""

    result = generate_response(prompt)
    return result