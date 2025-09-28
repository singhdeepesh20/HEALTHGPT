import streamlit as st
import os
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader


load_dotenv()
os.environ['HF_API_KEY'] = os.getenv("HF_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")


llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")


prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question.

<context>
{context}
</context>

Question: {input}
""")


def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader("data")
        st.session_state.docs = st.session_state.loader.load()

        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)


st.title("      HealthGPT      ")
user_prompt = st.text_input("Enter your question")

if st.button("Document_Embedding"):
    create_vector_embedding()
    st.success(" Vector Database is ready")

if user_prompt:
    if "vectors" not in st.session_state:
        st.warning("Please generate the vector DB first!")
    else:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        start = time.process_time()
        response = retrieval_chain.invoke({'input': user_prompt})
        end = time.process_time()

        st.markdown(f"** Response time:** `{end - start:.2f} seconds`")
        st.subheader(" Answer:")
        st.write(response.get('answer', 'No answer returned.'))

        with st.expander(" Retrieved Context Documents"):
            for i, doc in enumerate(response.get('context', [])):
                st.markdown(f"**Document {i+1}:**")
                st.write(doc.page_content)
                st.write('---')
