# RAG Assistant

A simple Retrieval-Augmented Generation (RAG) assistant built with Python. The project loads text documents, splits them into chunks, generates embeddings, stores them in a vector database, retrieves relevant context, and uses an LLM to answer user questions.

## Features

- Load `.txt` documents automatically
- Document chunking
- Embedding generation
- Vector store for semantic search
- Retrieval of relevant document chunks
- LLM-powered question answering
- Modular project structure

## Project Structure

```
app/
├── config/
├── controllers/
├── llm/
├── models/
├── services/
└── storage/

data/
├── raw/
├── chunks/
└── embedding.json
```

## Installation

Clone the repository:

```bash
git clone https://github.com/ayoub-bakr/rag_assistant.git
cd rag_assistant
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app/main.py
```

## Workflow

1. Load text documents
2. Split documents into chunks
3. Generate embeddings
4. Store embeddings
5. Retrieve relevant chunks
6. Generate answers using an LLM

## Technologies

- Python
- LangChain
- Vector Embeddings
- JSON Storage
- Retrieval-Augmented Generation (RAG)

## Future Improvements

- PDF support
- Multiple embedding models
- Vector databases (FAISS, Chroma, Pinecone)
- Web interface
- Conversation memory

## Author

Ayoub Bakr
