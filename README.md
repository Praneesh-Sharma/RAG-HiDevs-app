# **RAG-Based Document Retrieval System**  
A Streamlit-powered application that allows users to upload a PDF, extract embeddings, and query the document using an LLM for retrieval-augmented generation (RAG).  

---

## Features 
Upload a **PDF** and extract text chunks  
Store document embeddings in **ChromaDB**  
Use **LLM (via Groq API)** for answering queries  
Retrieve relevant document sections along with responses  
Built with **LangChain**, **ChromaDB**, and **Streamlit**  

---

## Installation & Setup 

### Clone the Repository 
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/RAG-Document-Retrieval.git
cd RAG-Document-Retrieval
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Setting Up API Keys (.env File)

To run the app, you need to set up your Groq API key. Create a .env file in the root directory:
```bash
touch .env  # Mac/Linux
echo GROQ_API_KEY=your_api_key_here > .env  # Windows (PowerShell)
```

Then, open the .env file and add:
```ini
GROQ_API_KEY=your_api_key_here
```
Replace your_api_key_here with your actual Groq API key.

### Running the Application
```bash
streamlit run app.py
```
This will launch the web app in your browser.

### Project Structure
```bash
📁 RAG-Document-Retrieval
│── 📄 app.py               # Streamlit UI
│── 📄 data_processing.py    # PDF processing & embedding generation
│── 📄 retrieval.py         # Querying LLM with document retrieval
│── 📄 requirements.txt     # Required dependencies
│── 📄 .env                 # API keys (ignored in Git)
│── 📁 venv/                # Virtual environment (not tracked)
└── 📂 data/                # (Optional) Store PDFs here
```
