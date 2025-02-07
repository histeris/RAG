import os
from typing import List
from PyPDF2 import PdfReader

def load_document(file_path: str) -> List[str]:
    """
    Load text from a PDF file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")

    
    text = []
    with open(file_path, "rb") as f:
        pdf_reader = PdfReader(f)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    
    return text


