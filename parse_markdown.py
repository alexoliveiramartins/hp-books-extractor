# https://github.com/pymupdf/pymupdf4llm <-HOLY FUCK

import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("./data/harrypotter_complete_edition.pdf")

pathlib.Path("./output/output.md").write_bytes(md_text.encode())