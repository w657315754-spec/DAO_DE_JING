#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR 转换脚本：将提取的 PDF 图片转换为 Markdown 文本
"""

import os
import sys
from pathlib import Path

# 添加必要的库
try:
    import pytesseract
    from PIL import Image
    import pdf2image
except ImportError as e:
    print(f"缺少必要的库：{e}")
    print("请安装：pip install pytesseract Pillow pdf2image")
    sys.exit(1)

def ocr_images_to_md(images_dir: str, output_md: str) -> None:
    """
    对目录中的所有图片进行 OCR 识别，并输出到 Markdown 文件
    """
    images_path = Path(images_dir)
    
    if not images_path.exists():
        print(f"图片目录不存在：{images_dir}")
        return
    
    # 获取所有图片文件，按名称排序
    image_files = sorted([
        f for f in images_path.iterdir() 
        if f.suffix.lower() in ['.jpg', '.jpeg', '.png']
    ])
    
    if not image_files:
        print(f"在 {images_dir} 中未找到图片文件")
        return
    
    print(f"找到 {len(image_files)} 张图片，开始 OCR 识别...")
    
    with open(output_md, 'w', encoding='utf-8') as md_file:
        md_file.write("# 炁体源流 - 上册（OCR 识别版）\n\n")
        md_file.write("---\n\n")
        
        for idx, img_path in enumerate(image_files, 1):
            print(f"处理第 {idx}/{len(image_files)} 张图片：{img_path.name}")
            
            try:
                # 打开图片
                img = Image.open(img_path)
                
                # 使用 pytesseract 进行 OCR 识别（中文）
                text = pytesseract.image_to_string(img, lang='chi_sim+eng')
                
                # 写入 Markdown 文件
                md_file.write(f"## 第 {idx} 页\n\n")
                md_file.write(text + "\n\n")
                md_file.write("---\n\n")
                
            except Exception as e:
                print(f"处理图片 {img_path.name} 时出错：{e}")
                md_file.write(f"## 第 {idx} 页\n\n")
                md_file.write(f"[OCR 识别失败：{e}]\n\n")
                md_file.write("---\n\n")
    
    print(f"OCR 识别完成！结果已保存到：{output_md}")

def main():
    # 设置图片目录和输出文件
    base_dir = Path(__file__).parent
    images_dir = base_dir / "images_upper"
    output_md = base_dir / "炁体源流 - 上册_OCR.md"
    
    # 执行 OCR 转换
    ocr_images_to_md(str(images_dir), str(output_md))

if __name__ == "__main__":
    main()
