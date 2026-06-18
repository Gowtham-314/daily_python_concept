<div align="center">

<img src="https://img.shields.io/badge/Python-3.9+-6D28D9?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Notebooks-Jupyter-7C3AED?style=for-the-badge" alt="Jupyter"/>
<img src="https://img.shields.io/badge/Status-Learning%20Collection-A855F7?style=for-the-badge" alt="Status"/>

</div>

---

## 📌 Overview

This repository is a curated collection of short, focused Python examples and notebooks for learning everyday Python concepts, file handling, basic data work, plotting, and PDF automation. Examples are intentionally small so you can open a notebook or script, run it, and learn a single concept in minutes.

---

## 📑 Table of Contents

- [What’s included](#-whats-included)
- [Project structure](#-project-structure)
- [Recommended learning order](#-recommended-learning-order)
- [Requirements](#-requirements)
- [Quick start](#-quick-start)
- [Notes](#-notes)
- [Author](#-author)

---

## 🧩 What’s included

- Short Jupyter notebooks and example scripts covering basic algorithms, function and argument patterns, working with files/paths, NumPy and Matplotlib basics, and a small PyMuPDF (PDF) playground.
- Example data files for hands-on exercises.

---

## 🗂️ Project structure

```
Daily_Python_Concept/
├── basic/
│   ├── Algorithm.ipynb
│   ├── args_kwargs.ipynb
│   ├── Decorators.ipynb
│   ├── Numpy.ipynb
│   └── student_data.json
├── file_path/
│   ├── file_path.ipynb
│   └── sample.txt
├── matplotlib/
│   └── learn_matplotlib.ipynb
├── mupdf/
│   ├── 01_basics/
│   ├── 02_text_extraction/
│   └── README.md
└── README.md
```

See individual directories for focused examples and short README notes (for example, `mupdf/README.md`).

---

## 🧭 Recommended learning order

1. Start in `basic/` notebooks to review Python fundamentals and small algorithmic examples.
2. Explore `file_path/` to practise reading/writing files and path operations.
3. Open `matplotlib/learn_matplotlib.ipynb` to learn plotting basics and visualization patterns.
4. Try `mupdf/` examples for PDF reading, extraction, and embedding experiments (see `mupdf/README.md`).

---

## ⚙️ Requirements

This workspace is notebook-first. Install the basics to run the examples locally:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
pip install --upgrade pip
pip install jupyterlab notebook numpy matplotlib pymupdf
```

Optional (only for the `mupdf/04_embedding` examples):

```powershell
pip install sentence-transformers scikit-learn faiss-cpu
```

---

## 🚀 Quick start

- Open the folder in VS Code or start Jupyter Lab from the repository root:

```powershell
jupyter lab
```

- Open any notebook and run cells interactively. For `.py` examples, run with Python:

```powershell
python mupdf/01_basics/open_pdf.py
```

---

## 📝 Notes

- Notebooks are designed to be read and executed cell-by-cell. Keep a dedicated virtual environment for dependencies.
- Some scripts produce output files (text exports, images, or modified PDFs) in their folders.

---

## 👨‍💻 Author

Made for personal learning and reference. If this repository helped you, consider keeping the examples and adapting them for your projects.

