from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
doc = fitz.open(pdf_path)

page = doc[0]   # First page

print(page.get_text())

doc.close()