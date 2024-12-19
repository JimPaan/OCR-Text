import pytesseract
from pdf2image import convert_from_path
import os

# PDF Input File
pdf_path = "iraya_paper.pdf"

# Convert PDF to Images
images = convert_from_path(pdf_path)

# OCR Text Extraction
extracted_text = ""
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    extracted_text += text + "\n"

# Save OCR Text to a File
with open("output_text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)

print("OCR Extraction Complete. Output saved to output_text.txt")
