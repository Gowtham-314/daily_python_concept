from pathlib import Path
import fitz

folder_path = Path(__file__).parent

pdf_path = Path("sample_files") / "sample.pdf"
doc = fitz.open(pdf_path)


page = doc[0]   # First page
pix = page.get_pixmap()
pix.save(f"{folder_path}/pdf_to_img_{page.number}.png")

doc.close()