#!/usr/bin/env python3
"""Extract images from PDF for OCR."""
import os
import pikepdf

pdf_path = "/Users/jim/workspace/try/DAO_DE_JING/张至顺教程/炁体源流/炁体源流-上册.pdf"
output_dir = "/Users/jim/workspace/try/DAO_DE_JING/张至顺教程/炁体源流/images_upper"
os.makedirs(output_dir, exist_ok=True)

with pikepdf.open(pdf_path) as pdf:
    img_count = 0
    for page_num, page in enumerate(pdf.pages, 1):
        if "/Resources" not in page:
            continue
        resources = page.Resources
        if "/XObject" not in resources:
            continue
        xobjects = resources.XObject
        for name, obj_ref in xobjects.items():
            try:
                obj = pdf.get_object(obj_ref.objgen)
                if obj.get("/Subtype") != "/Image":
                    continue
                width = int(obj.get("/Width", 0))
                height = int(obj.get("/Height", 0))
                filter_type = obj.get("/Filter")
                if filter_type == "/DCTDecode":
                    ext = "jpg"
                elif filter_type == "/FlateDecode":
                    ext = "png"
                else:
                    ext = "bin"
                raw_data = obj.read_raw_bytes()
                img_count += 1
                out_path = os.path.join(output_dir, f"page{page_num:03d}_{img_count:03d}.{ext}")
                with open(out_path, "wb") as f:
                    f.write(raw_data)
                print(f"Extracted: {out_path} ({width}x{height})")
            except Exception as e:
                print(f"Error on page {page_num}: {e}")

print(f"\nTotal images extracted: {img_count}")
