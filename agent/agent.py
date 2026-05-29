from agent.planner import create_plan
from agent.executor import execute_step
from memory.memory import add_to_memory, get_context


def run_agent(query):
    # Save user query
    add_to_memory("user", query)

    # Get past context
    context = get_context()

    # Step 1: Create Plan with memory
    plan = create_plan(context + "\nUser Query: " + query)

    steps = plan.split("\n")

    results = []

    # Step 2: Execute steps
    for step in steps[:3]:
        if step.strip() == "":
            continue

        result = execute_step(step)
        results.append(f"{step}\n{result}")

    final_answer = "\n\n".join(results)

    # Save response
    add_to_memory("assistant", final_answer)

    return final_answer