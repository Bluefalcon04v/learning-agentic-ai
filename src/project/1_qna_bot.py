from langchain.chat_models import init_chat_model

llm = init_chat_model("ollama:llama3.2")

import streamlit as st

st.title("AI QnA Bot")
st.markdown("My QnA bot with Langchain and Ollama!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask me anything")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    with st.chat_message("ai"):
        with st.spinner("Generating response..."):
            res = llm.invoke(query) 
            st.markdown(res.content)
            st.session_state.messages.append({"role": "ai", "content": res.content})