from pathlib import Path
import fitz

pdf_path = Path("sample_files") / "sample.pdf"
doc = fitz.open(pdf_path)

page = doc[0]   # First page

print(page.get_text())

doc.close()