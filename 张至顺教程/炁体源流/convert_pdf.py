#!/usr/bin/env python3
"""Convert PDF to Markdown using pdfplumber."""
import sys
import pdfplumber


def pdf_to_md(pdf_path: str, md_path: str) -> None:
    with pdfplumber.open(pdf_path) as pdf:
        with open(md_path, "w", encoding="utf-8") as out:
            for i, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    out.write(text)
                    out.write("\n\n")
                if i % 10 == 0:
                    print(f"  Processed {i}/{len(pdf.pages)} pages...")
    print(f"Done: {md_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert_pdf.py <input.pdf> <output.md>")
        sys.exit(1)
    pdf_to_md(sys.argv[1], sys.argv[2])
