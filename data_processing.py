import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def process_pdf(uploaded_file):
    """Extracts text from PDF and splits it into chunks."""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_text(text)

def create_embeddings(text_chunks):
    """Generates embeddings and stores them in ChromaDB."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma.from_texts(texts=text_chunks, embedding=embeddings)