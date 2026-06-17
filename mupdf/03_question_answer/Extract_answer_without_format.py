import fitz
from pathlib import Path

# pdf_path = Path(__file__).with_name("sample.pdf")
# if File is in same folder.

pdf_path = Path("sample_files") / "sample.pdf"

text = ""
with fitz.open(pdf_path) as doc:
    for page in doc:
        text += page.get_text()


# Split the text into chunks
chunk_size = 500
chunks = []
for i in range(0, len(text), chunk_size):
    chunks.append(
        text[i:i+chunk_size]
    )
    

# Create embeddings for each chunk

from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)


# Build a Vector Database using FAISS
import faiss
import numpy as np

embeddings = np.array(
    embeddings
).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)


# Querying the Vector Database
query = "What is machine learning?"
query_embedding = model.encode(
    [query]
).astype("float32")


# Search for the most similar chunks
distance, ids = index.search(
    query_embedding,
    k=3
)

print(ids)


for i in ids[0]:

    print("Answer:")

    print(chunks[i])

    print()