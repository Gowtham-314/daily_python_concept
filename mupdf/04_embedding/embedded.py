from pathlib import Path
import fitz

pdf_path = Path("sample_files") / "questions.pdf"
file_path = Path(__file__).parent
text = ""
with fitz.open(pdf_path) as doc:
    for page in doc:
        text += page.get_text()


# Split the text into chunks of 1000 characters

chunk_size = 1000
chunks = []
for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print(len(chunks))
    
    
# Generate embeddings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)
print(embeddings.shape)


# Save embeddings
import numpy as np
np.save(f"{file_path}/embeddings.npy",embeddings)


# Load embeddings
embeddings = np.load(
    f"{file_path}/embeddings.npy"
)

print("\n\n---- Loaded Embeddings ---")

query = "What is a database?"
query_embedding = model.encode(query)


from sklearn.metrics.pairwise import cosine_similarity

scores = cosine_similarity(
    [query_embedding],
    embeddings  
)

best_index = scores.argmax()

print(chunks[best_index])