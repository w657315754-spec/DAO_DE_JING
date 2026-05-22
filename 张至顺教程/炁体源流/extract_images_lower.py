#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取下册 PDF 中的图片
"""

import pikepdf
from pathlib import Path

base_dir = Path("/Users/jim/workspace/try/DAO_DE_JING/张至顺教程/炁体源流")
output_dir = base_dir / "images_lower"
output_dir.mkdir(exist_ok=True)

pdf_files = list(base_dir.glob("*下册*.pdf"))
if not pdf_files:
    print("未找到下册 PDF 文件")
    exit(1)

pdf_path = pdf_files[0]
print(f"PDF 路径：{pdf_path}")

with pikepdf.open(str(pdf_path)) as pdf:
    img_count = 0
    for page_num, page in enumerate(pdf.pages, 1):
        if "/Resources" not in page or "/XObject" not in page.Resources:
            continue
        xobjects = page.Resources.XObject
        for name, obj_ref in xobjects.items():
            obj = pdf.get_object(obj_ref.objgen)
            if obj.get("/Subtype") == "/Image":
                ext = "jpg" if obj.get("/Filter") == "/DCTDecode" else "png"
                raw_data = obj.read_raw_bytes()
                img_count += 1
                out_path = output_dir / f"page{page_num:03d}_{img_count:03d}.{ext}"
                with open(str(out_path), "wb") as f:
                    f.write(raw_data)
                print(f"提取：{out_path.name}")

print(f"\n共提取 {img_count} 张图片到 {output_dir}")