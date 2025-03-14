import streamlit as st
from data_processing import process_pdf, create_embeddings
from retrieval import query_documents

st.title("RAG-based Document Retrieval & Answering")

# File Upload Section
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    # Process PDF and create embeddings
    text_chunks = process_pdf(uploaded_file)
    db = create_embeddings(text_chunks)

    st.success("Text processing complete! Ready for queries.")

    # Query Section
    user_query = st.text_input("Ask a question based on the document:")
    if user_query:
        response, sources = query_documents(user_query, db)
        
        st.write("### Answer:")
        st.write(response)
        
        st.write("### Relevant Document Chunks:")
        for chunk in sources:
            st.write(chunk.page_content)