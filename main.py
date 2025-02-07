import os
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Depends
from ingestion import load_document, process_text, store_embeddings, search_embeddings
import time
import logging
from langchain_ollama import OllamaEmbeddings

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()


UPLOAD_DIR = "uploads"
VECTOR_STORE_DIR = "vector_data"
DATA_DIR = "data"

for directory in [UPLOAD_DIR, VECTOR_STORE_DIR, DATA_DIR]:
    os.makedirs(directory, exist_ok=True)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400,detail="Uploaded file is empty")
        # save uploaded file
        with open(file_path, "wb") as f:
            f.write(content)

    
        logging.info(f"Processing file: {file.filename}")
        # Load document text
        text_data = load_document(file_path)
        logging.info("Document loaded successfully.")
        # process text into chunks
        text_chunks = process_text(text_data)
        logging.info(f"Document split into {len(text_chunks)} chunks.")
        # Store in vector database
        store_embeddings(text_chunks)
        logging.info("Embeddings stored successfully.")
        
        return {"message": f"Document {file.filename} processed and stored."}
    except Exception as e:
        logging.error(f"Error processing document: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time()- start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

llm = OllamaEmbeddings(model="llama3")

@app.post("/query/")
async def query_rag(question: str):
    try:
        
        relevant_docs = search_embeddings(question, k=3)  
        
        if not relevant_docs:
            return {"message": "No relevant documents found.", "answer": "I couldn't find any relevant information."}

        
        context_text = "\n\n".join([doc.page_content for doc in relevant_docs])
        prompt = f"Context:\n{context_text}\n\nQuestion: {question}\nAnswer:"

        
        response = llm.embed_query(prompt)

        
        sources = [doc.metadata.get("source", "Unknown source") for doc in relevant_docs]
        return {"answer": response, "sources": sources}

    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
