import os
import pickle
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from datetime import datetime

# UPGRADED MODEL: BGE-Base
EMBEDDING_MODEL_NAME = 'BAAI/bge-base-en-v1.5'

def process_pdf(pdf_path, index_path, metadata_path):
    print(f"Reading {pdf_path}...")
    reader = PdfReader(pdf_path)
    file_name = os.path.basename(pdf_path)
    last_updated = datetime.fromtimestamp(os.path.getmtime(pdf_path)).strftime('%Y-%m-%d %H:%M:%S')
    
    all_chunks = []
    all_metadata = []
    
    chunk_size = 700
    overlap = 150 # Increased overlap for better context
    
    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if not page_text:
            continue
        page_text = " ".join(page_text.split())
        
        for i in range(0, len(page_text), chunk_size - overlap):
            chunk = page_text[i:i + chunk_size]
            all_chunks.append(chunk)
            all_metadata.append({
                "text": chunk,
                "page_number": page_num + 1,
                "file_name": file_name,
                "last_updated": last_updated
            })
    
    print(f"Total chunks created: {len(all_chunks)}")
    
    print(f"Loading UPGRADED embedding model: {EMBEDDING_MODEL_NAME}...")
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    
    # BGE models work best with this instruction for indexing
    embeddings = model.encode(all_chunks, normalize_embeddings=True)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) # Inner Product is better for BGE
    index.add(np.array(embeddings).astype('float32'))
    
    faiss.write_index(index, index_path)
    with open(metadata_path, 'wb') as f:
        pickle.dump(all_metadata, f)
    
    print(f"SUCCESS: Rebuilt index with {EMBEDDING_MODEL_NAME}")

if __name__ == "__main__":
    process_pdf("Articles.pdf", "index.faiss", "metadata.pkl")
