# Simple in-memory storage

conversation_history = []

MAX_MEMORY=20
def add_to_memory(role, content):
    conversation_history.append({
        "role": role,
        "content": content
    })
    # Limit memory to MAX_MEMORY
    if len(conversation_history) > MAX_MEMORY:
        conversation_history.pop(0)


def get_memory():
    return conversation_history


def get_context():
    """
    Convert memory into prompt format
    """
    context = ""
    for msg in conversation_history[-5:]:  # last 5 messages
        context += f"{msg['role']}: {msg['content']}\n"

    return context