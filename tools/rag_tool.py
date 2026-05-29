import PyPDF2
from vectorstore.vectordb import add_documents, search
from llm.llm import generate_response


def load_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks


def process_pdf(file):
    text = load_pdf(file)
    chunks = chunk_text(text)
    add_documents(chunks)


def rag_query(query):
    docs = search(query)

    context = "\n".join(docs)

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}
"""

    return generate_response(prompt)