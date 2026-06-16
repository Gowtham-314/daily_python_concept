from pathlib import Path
import fitz

pdf_path = Path(__file__).with_name("sample.pdf")
doc = fitz.open(pdf_path)

maintext = ""
for page in doc:
    text = page.get_text()
    print(text)
    maintext = maintext + text

with open(Path(__file__).with_name(f"openpdf.txt"), "w", encoding="utf-8") as f:
    f.write(maintext)

doc.close()