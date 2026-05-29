from llm.llm import generate_response


def create_plan(query):
    prompt = f"""
You are an AI research planner.

Break this query into step-by-step research tasks.

If information requires latest or real-world data, include the word "search" in that step.

Query: {query}

Return only numbered steps.
"""

    plan = generate_response(prompt)
    return plan