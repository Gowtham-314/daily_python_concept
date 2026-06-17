import re

from pathlib import Path
import fitz


pdf_path = Path("sample_files") / "questions.pdf"
target_question = "What is Machine Learning?"

doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text()

doc.close()

pattern = rf"{re.escape(target_question)}\s*Answer:\s*(.*?)(?=Q\d+\.|$)"

match = re.search(pattern, text, re.DOTALL)

if match:
    answer = match.group(1).strip()
    print(f"Question: {target_question}\n")
    print(answer)
else:
    print("Question not found.")