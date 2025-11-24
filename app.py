import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
import time

#  DIRECT API KEY (no .env)
groq_api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Initialize on first run
if "vectors" not in st.session_state:
    # FIXED: Add model parameter to OllamaEmbeddings
    st.session_state.embeddings = OllamaEmbeddings(model="all-minilm")

    st.session_state.loader = WebBaseLoader(
        "https://www.geeksforgeeks.org/machine-learning/machine-learning/"
    )
    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(
        st.session_state.docs[:50]
    )

    st.session_state.vectors = FAISS.from_documents(
        st.session_state.final_documents,
        st.session_state.embeddings
    )

st.title("ChatGroq Inference Engine")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.

    <context>
    {context}
    </context>

    Question: {input}
    """
)


def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


retriever = st.session_state.vectors.as_retriever()

document_chain = (
    {
        "context": retriever | format_docs,
        "input": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

user_prompt = st.text_input("Input your prompt here")

if user_prompt:
    start = time.time()
    response = document_chain.invoke(user_prompt)
    print("Response time:", time.time() - start)
    st.write(response)

    with st.expander("Document Similarity Search"):
        context_docs = retriever.invoke(user_prompt)
        for i, doc in enumerate(context_docs):
            st.write(doc.page_content)
            st.write("--------------------------------")
