from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
word = "characteristics of an operational amplifier"

with fitz.open(pdf_path) as doc:
    
    for page_num, page in enumerate(doc, start=1):

        text = page.get_text()

        if word.lower() in text.lower():

            print(f"\n----- Page {page_num} -----")
            print(text)
