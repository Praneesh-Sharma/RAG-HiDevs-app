import os
import groq
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # Load API key

def query_documents(query, db):
    """Query LLM with retrieval."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Set it in .env or as an environment variable.")

    # Try available models
    try:
        llm = ChatGroq(model_name="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))  # Change if needed
    except groq.NotFoundError:
        llm = ChatGroq(model_name="mixtral-8x7b", api_key=api_key)  # Alternative model

    retriever = db.as_retriever()
    response = llm.invoke(query)
    
    return response, retriever.get_relevant_documents(query)
