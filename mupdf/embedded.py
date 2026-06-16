from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
doc = fitz.open(pdf_path)

text = ""
for page in doc:
    text += page.get_text()

doc.close()


# Split the text into chunks of 1000 characters

chunk_size = 1000

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print(len(chunks))

for chunk in chunks:
    print(chunk)
    print("-" * 40)