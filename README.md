# Retrieval-Augmented Generation (RAG) System
# Overview
This project is an implementation of a Retrieval-Augmented Generation (RAG) system using Python, FastAPI, LangChain, FAISS, and Ollama. The system enables users to search document-based information and integrate it with an LLM model to generate more contextual answers.
# Technology Stack Requirements
- Python 
- FastAPI 
- LangChain 
- FAISS 
- Ollama 
- Docker 
# Installation
## 1️⃣ Clone Repository
````
git clone https://github.com/your-repo/rag-project.git
cd rag-project
````
## 2️⃣ Install Dependencies
Use a virtual environment:
````
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
````
Then install dependencies:
````
pip install -r requirements.txt
````
## 3️⃣ Run FastAPI
````
uvicorn main:app --reload
````
The server will run at http://127.0.0.1:8000.
## 4️⃣ Check API Docs
Open a browser and access:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

# Features
## 1️⃣ Upload Documents 
Upload PDF or text files to be indexed in FAISS.
## 2️⃣ Vector Search with FAISS 
Uses FAISS to retrieve relevant documents based on user queries.
## 3️⃣ Retrieval-Augmented Generation (RAG) 
Uses LangChain and Ollama to generate answers based on retrieved documents.
## 4️⃣ Docker Support 
The project supports Docker for easier deployment.

# API Endpoints
## 1️⃣ Upload Documents
Endpoint:
````
POST /upload/
````
Request Body:
````
{
  "file": "yourfile.pdf"
}
````
## 2️⃣ Query System
Endpoint:
````
POST /query/?question={your_question}
````
Example:
````
curl -X 'POST' 'http://127.0.0.1:8000/query/?question=What is AI?' -H 'accept: application/json'
````
## 3️⃣ List Stored Documents
Endpoint:
````
GET /documents/
````
# Running with Docker
## 1️⃣ Build Docker Image
````
docker build -t rag-system .
````
## 2️⃣ Run Container
````
docker run -p 8000:8000 rag-system
````
# Troubleshooting
If you encounter the error "'str' object has no attribute 'page_content'", try the following steps:

1️. Ensure FAISS has a valid index.

2️. Check if the query search returns a Document object.

3️. Reset FAISS storage with:
````
rm -r vector_data/
````
