from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.docstore.document import Document
import os
import pickle

VECTOR_STORE_DIR = "vector_data"
INDEX_FILE = os.path.join(VECTOR_STORE_DIR, "faiss_index")
METADATA_FILE = os.path.join(VECTOR_STORE_DIR, "metadata.pkl")


os.makedirs(VECTOR_STORE_DIR, exist_ok=True)


embedding_model = OllamaEmbeddings(model="llama3")

faiss_index = None  
metadata = []

try:
    if os.path.exists(INDEX_FILE):
        faiss_index = FAISS.load_local(VECTOR_STORE_DIR, embedding_model)
        # print("Loading existing FAISS index...")
        
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "rb") as f:
            metadata = pickle.load(f)
        # print("Metadata loaded successfully.")
        

except Exception as e:
    print(f"Error loading FAISS or metadata: {e}")
    faiss_index = None
    metadata = []


def store_embeddings(text_chunks):
    """Menyimpan embeddings dari potongan teks ke FAISS index."""
    global faiss_index, metadata

    if not text_chunks:
        return "No text chunks provided"


    print(f"Received text chunks: {text_chunks}")

    new_docs = [Document(page_content=chunk) for chunk in text_chunks if isinstance(chunk, str) and chunk.strip()]
    

    print(f"Documents to store: {new_docs}")

    if not new_docs:
        return "All text already in FAISS or invalid input."

    if faiss_index is None:
        faiss_index = FAISS.from_documents(new_docs, embedding_model)
    else:
        faiss_index.add_documents(new_docs)

    metadata.extend(text_chunks)


    faiss_index.save_local(VECTOR_STORE_DIR)
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)

    return "Embeddings stored successfully"


def search_embeddings(query, k=3):
    """Mencari dokumen yang paling relevan berdasarkan query."""
    global faiss_index

    if faiss_index is None:
        return ["FAISS index has not been created. Please upload documents first."]

    try:
        search_results = faiss_index.similarity_search(query, k)

        # Debugging log
        print(f"Search results type: {type(search_results)}")
        print(f"Search results: {search_results}")

        if isinstance(search_results, list) and all(isinstance(doc, Document) for doc in search_results):


            return search_results  
        else:
            return ["Unexpected result format. Please check your FAISS index."]

    except Exception as e:
        return [f"An error occurred while searching: {e}"]


