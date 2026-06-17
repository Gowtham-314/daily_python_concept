from pathlib import Path
import fitz

pdf_path = Path("sample_files") / "sample.pdf"
word = "characteristics of an operational amplifier"

with fitz.open(pdf_path) as doc:

    for page_num, page in enumerate(doc, start=1):

        lines = page.get_text().split("\n")

        for line in lines:

            if word.lower() in line.lower():

                print(f"Page {page_num}: {line}")
