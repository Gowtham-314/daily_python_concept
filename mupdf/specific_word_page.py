from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
word = "characteristics of an operational amplifier"

with fitz.open(pdf_path) as doc:
    
    pages_found = []
    for page_num in range(len(doc)):
        page = doc[page_num]

        matches = page.search_for(word)

        if matches:
            pages_found.append(page_num + 1)

print(f'"{word}" found on pages:', pages_found)