import cv2
import pytesseract
from pdf2image import convert_from_path
import numpy as np

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# PDF path
pdf_path = r"C:\Users\hp\Desktop\Python Training\PDFsCODE\REC & BILL-1.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_path)

all_text = ""

for i, page in enumerate(pages):

    # Convert PIL image to numpy array
    img = np.array(page)

    # Convert RGB → BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold
    thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # OCR
    text = pytesseract.image_to_string(thresh)

    print(f"\n--- PAGE {i+1} ---\n")
    print(text)

    all_text += text + "\n"

# Save output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("\nDone")