# RAG
Retrieval-Augmented Generation (RAG) System📌 OverviewThis project is an implementation of a Retrieval-Augmented Generation (RAG) system using Python, FastAPI, LangChain, FAISS, and Ollama. The system enables users to search document-based information and integrate it with an LLM model to generate more contextual answers.
🛠️ Tech StackPython 3.7+
FastAPI (Backend API)
LangChain (Framework for RAG)
FAISS (Vector Store for fast retrieval)
Ollama (LLM for answering queries)
Docker (For containerization)
⚙️ Installation1️⃣ Clone Repositorygit clone https://github.com/your-repo/rag-project.git
cd rag-project2️⃣ Install DependenciesUse a virtual environment:
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For WindowsThen install dependencies:
pip install -r requirements.txt3️⃣ Run FastAPIuvicorn main:app --reloadThe server will run at http://127.0.0.1:8000.
4️⃣ Check API DocsOpen a browser and access:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
🚀 Features1️⃣ Upload Documents 📂
Upload PDF or text files to be indexed in FAISS.
2️⃣ Vector Search with FAISS 🔍
Uses FAISS to retrieve relevant documents based on user queries.
3️⃣ Retrieval-Augmented Generation (RAG) 🤖
Uses LangChain and Ollama to generate answers based on retrieved documents.
4️⃣ Docker Support 🐳
The project supports Docker for easier deployment.
📜 API Endpoints1️⃣ Upload DocumentsEndpoint:
POST /upload/Request Body:
{
  "file": "yourfile.pdf"
}2️⃣ Query SystemEndpoint:
POST /query/?question={your_question}Example:
curl -X 'POST' 'http://127.0.0.1:8000/query/?question=What is AI?' -H 'accept: application/json'3️⃣ List Stored DocumentsEndpoint:
GET /documents/🐳 Running with Docker1️⃣ Build Docker Imagedocker build -t rag-system .2️⃣ Run Containerdocker run -p 8000:8000 rag-system🛠️ TroubleshootingIf you encounter the error "'str' object has no attribute 'page_content'", try the following steps:
1️⃣ Ensure FAISS has a valid index.
2️⃣ Check if the query search returns a Document object.
3️⃣ Reset FAISS storage with:
rm -r vector_data/📝 To-Do List✅ Implement FAISS for retrieval
✅ Integrate Ollama for RAG
⬜️ Implement authentication
⬜️ Deploy to cloud
📄 LicenseMIT License
📬 ContactFor questions, contact: your.email@example.com or create an issue in this repository!
