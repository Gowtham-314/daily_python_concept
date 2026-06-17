<div align="center">

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPwv_SifrjxsFJ3I_gP-mK4pwcL8aX5QGKXYbRBqPBOA&s=10" width="5%"/>

<p>
<img src="https://img.shields.io/badge/Python-3.9+-6D28D9?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/PyMuPDF-fitz-7C3AED?style=for-the-badge" alt="PyMuPDF"/>
<img src="https://img.shields.io/badge/Embeddings-Semantic%20Search-8B5CF6?style=for-the-badge" alt="Embeddings"/>
<img src="https://img.shields.io/badge/Status-Learning%20Project-A855F7?style=for-the-badge" alt="Status"/>
</p>

*A hands-on playground for mastering PDF automation, text extraction, and semantic search with PyMuPDF.*

</div>

---

## 📑 Table of Contents

- [✨ Overview](#-overview)
- [📚 What You Will Learn](#-what-you-will-learn)
- [🗂️ Project Structure](#-project-structure)
- [🧭 Recommended Learning Order](#-recommended-learning-order)
- [⚙️ Requirements](#-requirements)
- [🚀 Quick Start](#-quick-start)
- [📝 Notes](#-notes)
- [👨‍💻 Author](#-author)

---

## ✨ Overview

This repository is a hands-on learning space for working with PDFs in Python using [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`). It walks through opening PDFs, extracting text, searching for specific content, modifying pages, rendering images, and building a lightweight embedding-based semantic search workflow — all in small, focused scripts you can read end-to-end in minutes.

---

## 📚 What You Will Learn

| | Skill |
|:---:|---|
| 📖 | Open and read PDF files with Python |
| 🔍 | Extract text from a full PDF, a single page, or matching lines and words |
| 🧭 | Search for specific content across pages |
| ✏️ | Modify a PDF by inserting new text |
| 🖼️ | Convert PDF pages into images |
| ❓ | Build a basic question-answer extraction workflow |
| 🧠 | Generate and use embeddings for semantic search |

---

## 🗂️ Project Structure

```
mupdf-python-examples/
├── 01_basics/
│   ├── open_pdf.py
│   ├── open_specific_page.py
│   ├── alter_pdf.py
│   ├── pdf_to_img.py
│   └── openpdf.txt
├── 02_text_extraction/
│   ├── specific_line.py
│   ├── specific_word_page.py
│   └── specific_word_page_extract.py
├── 03_question_answer/
│   ├── Extract_answer.py
│   ├── Extract_answer_with_format.py
│   └── Extract_answer_without_format.py
├── 04_embedding/
│   ├── embedded.py
│   └── embeddings.npy
├── sample_files/
│   ├── sample.pdf
│   └── questions.pdf
└── README.md
```

<details>
<summary><strong>📁 01_basics</strong> — core PDF operations and beginner-friendly examples</summary>
<br>

| File | Description |
|---|---|
| [`open_pdf.py`](01_basics/open_pdf.py) | Opens a sample PDF and extracts text from every page |
| [`open_specific_page.py`](01_basics/open_specific_page.py) | Reads text from the first page only |
| [`alter_pdf.py`](01_basics/alter_pdf.py) | Inserts new text into a PDF and saves the edited file |
| [`pdf_to_img.py`](01_basics/pdf_to_img.py) | Converts a PDF page into an image |
| [`openpdf.txt`](01_basics/openpdf.txt) | Plain-text output generated from the full PDF extraction example |

</details>

<details>
<summary><strong>📁 02_text_extraction</strong> — finding specific content inside PDF text</summary>
<br>

| File | Description |
|---|---|
| [`specific_line.py`](02_text_extraction/specific_line.py) | Searches extracted text line by line for a target phrase |
| [`specific_word_page.py`](02_text_extraction/specific_word_page.py) | Finds the page numbers that contain a target phrase |
| [`specific_word_page_extract.py`](02_text_extraction/specific_word_page_extract.py) | Prints the full text of pages containing a target phrase |

</details>

<details>
<summary><strong>📁 03_question_answer</strong> — extracting answers from Q&A-style PDFs</summary>
<br>

| File | Description |
|---|---|
| [`Extract_answer.py`](03_question_answer/Extract_answer.py) | Extracts the answer for a specific question using regex |
| [`Extract_answer_with_format.py`](03_question_answer/Extract_answer_with_format.py) | Same idea as above, with formatted output |
| [`Extract_answer_without_format.py`](03_question_answer/Extract_answer_without_format.py) | A more direct answer-extraction version |

</details>

<details>
<summary><strong>📁 04_embedding</strong> — semantic search and vector embedding examples</summary>
<br>

| File | Description |
|---|---|
| [`embedded.py`](04_embedding/embedded.py) | Chunks PDF text, creates embeddings, saves and reloads them, and retrieves the closest match for a query |
| [`embeddings.npy`](04_embedding/embeddings.npy) | Saved embedding vectors produced by the embedding example |

</details>

<details>
<summary><strong>📁 sample_files</strong> — practice PDFs used across the examples</summary>
<br>

| File | Description |
|---|---|
| [`sample.pdf`](sample_files/sample.pdf) | Main sample document used by the basics and text extraction scripts |
| [`questions.pdf`](sample_files/questions.pdf) | Sample question-answer document used by the extraction and embedding scripts |

</details>

---

## 🧭 Recommended Learning Order

| Step | Focus | Start Here |
|:---:|---|---|
| 1 | Open and read PDFs | [`open_pdf.py`](01_basics/open_pdf.py), [`open_specific_page.py`](01_basics/open_specific_page.py) |
| 2 | Search for content inside text | [`specific_line.py`](02_text_extraction/specific_line.py), [`specific_word_page.py`](02_text_extraction/specific_word_page.py) |
| 3 | Extract answers from Q&A documents | Scripts in [`03_question_answer`](03_question_answer) |
| 4 | Explore semantic search with embeddings | [`embedded.py`](04_embedding/embedded.py) |

---

## ⚙️ Requirements

<p>
<img src="https://img.shields.io/badge/pymupdf-6D28D9?style=flat-square" alt="pymupdf"/>
<img src="https://img.shields.io/badge/sentence--transformers-7C3AED?style=flat-square" alt="sentence-transformers"/>
<img src="https://img.shields.io/badge/numpy-8B5CF6?style=flat-square" alt="numpy"/>
<img src="https://img.shields.io/badge/scikit--learn-A855F7?style=flat-square" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/faiss--cpu-6D28D9?style=flat-square" alt="faiss-cpu"/>
</p>

```bash
pip install pymupdf sentence-transformers numpy scikit-learn faiss-cpu
```

> `faiss-cpu` works on most machines — swap in `faiss` if you have a build suited to your platform.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Gowtham-314/mupdf-python-examples.git
cd mupdf-python-examples

# Install dependencies
pip install pymupdf sentence-transformers numpy scikit-learn faiss-cpu

# Run your first example
python 01_basics/open_pdf.py
```

---

## 📝 Notes

- Running the scripts generates output files such as [`01_basics/openpdf.txt`](01_basics/openpdf.txt), [`04_embedding/embeddings.npy`](04_embedding/embeddings.npy), or an edited PDF named `output.pdf`.
- Every example is intentionally small and self-contained, so it's easy to adapt for your own PDF automation experiments.

---


## 👨‍💻 Author

<p>
<a href="https://github.com/Gowtham-314">
<img src="https://img.shields.io/badge/GitHub-Gowtham--314-6D28D9?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
</p>

If this helped you learn PyMuPDF, consider starring the repo ⭐

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6D28D9,100:A855F7&height=120&section=footer" width="100%"/>
</div>