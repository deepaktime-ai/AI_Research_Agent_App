import streamlit as st
from tools.rag_tool import process_pdf
from agent.agent import run_agent

# --- 1. PAGE CONFIG (MUST BE FIRST) ---
st.set_page_config(page_title="AI Research Agent", layout="wide")

# --- 2. HEADER & UI ---
st.title("🧠 AI Research Agent")
st.write("Ask any research question...")

# --- 3. SIDEBAR / FILE UPLOADER ---
with st.sidebar:
    st.header("Upload Documents")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file:
        process_pdf(uploaded_file)
        st.success("PDF processed successfully!")

# --- 4. SESSION STATE FOR CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 5. DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- 6. USER INPUT & AGENT EXECUTION ---
user_input = st.chat_input("Enter your research query...")

if user_input:
    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Run the agent
    with st.chat_message("assistant"):
        response = run_agent(user_input)
        st.write(response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
