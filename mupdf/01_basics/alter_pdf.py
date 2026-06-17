from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
doc = fitz.open(pdf_path)

page = doc[0]

page.insert_text(
    (100, 200),
    "This is some new text added to the PDF file.",
    fontsize=12
)

doc.save(f"{pdf_path.parent}/output.pdf")
doc.close()