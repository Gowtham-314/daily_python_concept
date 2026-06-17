from pathlib import Path
import fitz


pdf_path = Path("sample_files") / "questions.pdf"

with fitz.open(pdf_path) as doc:
    text = ""
    for page in doc:
        text += page.get_text()
        
target_question = input("Enter the word to search for: ")

for texts in text.splitlines():
    if target_question.lower() in texts.lower():
        print(f"Found: {texts}")
else:
    print(f"Not found:")