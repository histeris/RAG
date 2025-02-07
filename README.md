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
# Example
### Input uploading file
Final Exam Entrepreneurship Market Validation_Rafaell Widjaya_26021655511_eShelf.pdf
### Output
````
2025-02-07 11:07:57,160 - INFO - Processing file: Final Exam Entrepreneurship Market Validation_Rafaell Widjaya_26021655511_eShelf.pdf
2025-02-07 11:07:57,242 - INFO - Document loaded successfully.
2025-02-07 11:07:57,243 - INFO - Document split into 4 chunks.
Received text chunks: ["Business Model Canva\nWhy Use eShelf?\n Features\nResources\nEstimated Cost\n5W1H Market Validation\nReflection\nThe validation brought important insights regarding the needs and expectations of the market from EShelf as an online bookstore management solution. We've come to know, through\nsurvey analysis, interviews, and the testing of MVPs, that a simple UI and automation of inventory are the strengths of our product. However, search and filter are still under developed,", 'there are still minor bugs that need fixing, and limited payment options. The validation helps us understand the needs of the target market and highlights how important it is to listen to\ncustomers while developing a product. Moreover, market research shows the prospect of cooperation with publishers and local bookstores is still very high, especially for the customer', 'segment which has not been served well. To reflect, we understand that further development should be focused on the refinement of core features, design improvement, the addition of\npayment options, and logistics process optimization. By doing so, EShelf will become a platform able to satisfy the needs of users, support the growth of local bookstore businesses, and\nbring substantial added value to the market.', 'bring substantial added value to the market.\nBisanara Product WebpageeShelf2602165221 - Michael Matthew Muliawan . 2602164710 - Rico Herald Cenniago . 2602165511 -\nRafaell Widjaya . 2602165234 - Eric JevonEntrepreneurship Market Validation Group 4\neShelf is an online bookstore managing system that helps bookstore owners sell and distribute physical and digital books. It\nsimplifies book searches, purchases, and inventory management for customers and businesses alike.\nProblem']
Documents to store: [Document(metadata={}, page_content="Business Model Canva\nWhy Use eShelf?\n Features\nResources\nEstimated Cost\n5W1H Market Validation\nReflection\nThe validation brought important insights regarding the needs and expectations of the market from EShelf as an online bookstore management solution. We've come to know, through\nsurvey analysis, interviews, and the testing of MVPs, that a simple UI and automation of inventory are the strengths of our product. However, search and filter are still under developed,"), Document(metadata={}, page_content='there are still minor bugs that need fixing, and limited payment options. The validation helps us understand the needs of the target market and highlights how important it is to listen to\ncustomers while developing a product. Moreover, market research shows the prospect of cooperation with publishers and local bookstores is still very high, especially for the customer'), Document(metadata={}, page_content='segment which has not been served well. To reflect, we understand that further development should be focused on the refinement of core features, design improvement, the addition of\npayment options, and logistics process optimization. By doing so, EShelf will become a platform able to satisfy the needs of users, support the growth of local bookstore businesses, and\nbring substantial added value to the market.'), Document(metadata={}, page_content='bring substantial added value to the market.\nBisanara Product WebpageeShelf2602165221 - Michael Matthew Muliawan . 2602164710 - Rico Herald Cenniago . 2602165511 -\nRafaell Widjaya . 2602165234 - Eric JevonEntrepreneurship Market Validation Group 4\neShelf is an online bookstore managing system that helps bookstore owners sell and distribute physical and digital books. It\nsimplifies book searches, purchases, and inventory management for customers and businesses alike.\nProblem')]
2025-02-07 11:08:21,054 - INFO - Failed to load GPU Faiss: name 'GpuIndexIVFFlat' is not defined. Will not load constructor refs for GPU indexes.
ot load constructor refs for GPU indexes.
2025-02-07 11:08:21,089 - INFO - Embeddings stored successfully.
````
### Input for question
````
What features still need to be developed in EShelf?
````
### Output for question
````
2025-02-07 11:10:24,303 - INFO - HTTP Request: POST http://127.0.0.1:11434/api/embed "HTTP/1.1 200 OK"  
Search results type: <class 'list'>
Search results: [Document(id='1baf2768-945d-48cc-a83b-9ae38d910379', metadata={}, page_content='segment which has not been served well. To reflect, we understand that further development should be focused on the refinement of core features, design improvement, the addition of\npayment options, and logistics process optimization. By doing so, EShelf will become a platform able to satisfy the needs of users, support the growth of local bookstore businesses, and\nbring substantial added value to the market.'), Document(id='fc4c45b6-417d-4348-add8-c0b1b712449f', metadata={}, page_content='bring substantial added value to the market.\nBisanara Product WebpageeShelf2602165221 - Michael Matthew Muliawan . 2602164710 - Rico Herald Cenniago . 2602165511 -\nRafaell Widjaya . 2602165234 - Eric JevonEntrepreneurship Market Validation Group 4\neShelf is an online bookstore managing system that helps bookstore owners sell and distribute physical and digital books. It\nsimplifies 2025-02-07 11:10:28,904 - INFO - HTTP Request: POST http://127.0.0.1:11434/api/embed "HTTP/1.1 200 OK"
````
# Notes
The answer can be viewed via terminal
