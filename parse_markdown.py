# https://github.com/pymupdf/pymupdf4llm <-HOLY FUCK

import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("./data/hp-epub.epub")

pathlib.Path("./output/output_epub.md").write_bytes(md_text.encode())