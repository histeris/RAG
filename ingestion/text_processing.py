from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_text(text_list, chunk_size=500, chunk_overlap=50):
    """Split text into chunks for embedding."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(" ".join(text_list))
