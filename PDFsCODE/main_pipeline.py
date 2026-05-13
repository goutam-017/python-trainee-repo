import pdfplumber
import fitz
import camelot
from PIL import Image
import pytesseract
from PyPDF2 import PdfReader
import io
import os


# ==========================================
# DETECT PDF TYPE
# ==========================================

def detect_pdf_type(pdf_path):
    reader = PdfReader(pdf_path)
    if reader.is_encrypted:
        return "encrypted"

    pdf_info={
    "text_found":False,
    "image_found":False,
    "table_found":False
    }

    # -------------------------
    # Check text
    # -------------------------
    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text and text.strip():
                pdf_info["text_found"] = True
                break

    # -------------------------
    # Check image
    # -------------------------
    doc = fitz.open(pdf_path)

    for page in doc:

        images = page.get_images()

        if len(images) > 0:
            pdf_info["image_found"] = True
            break

    # -------------------------
    # Check tables
    # -------------------------
    try:
        tables = camelot.read_pdf(
            pdf_path,
            pages="1",
            flavor="stream"
        )

        if tables.n > 0:
            pdf_info["table_found"] = True
    except:
        pass
    return pdf_info

# EXTRACT TEXT PDF

def extract_text_pdf(pdf_path):

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text

# EXTRACT SCANNED PDF

def extract_scanned_pdf(pdf_path):

    full_text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        pix = page.get_pixmap()

        img_bytes = pix.tobytes("png")

        image = Image.open(io.BytesIO(img_bytes))

        text = pytesseract.image_to_string(image)

        full_text += text + "\n"

    return full_text

# EXTRACT TABLE PDF

def extract_table_pdf(pdf_path):

    full_text = ""

    tables = camelot.read_pdf(
        pdf_path,
        pages="all",
        flavor="stream"
    )

    for i, table in enumerate(tables):

        df = table.df

        full_text += f"\n========== TABLE {i+1} ==========\n\n"

        full_text += df.to_string(index=False)

        full_text += "\n"

    return full_text

# SAVE TXT FILE

def save_txt(text, output_file):

    with open(output_file, "w", encoding="utf-8") as f:

        f.write(text)

    print(f"\nSaved : {output_file}")

# MAIN PIPELINE

def pdf_pipeline(pdf_path):

    pdf_type = detect_pdf_type(pdf_path)

    print(f"\nDetected PDF Type : {pdf_type}")

    os.makedirs("PDFsCODE_output", exist_ok=True)

    # TEXT PDF

    if pdf_type["text_found"]:

        text = extract_text_pdf(pdf_path)

        save_txt(
            text,
            "PDFsCODE_output/text_pdf_chunk.txt"
        )

    # SCANNED PDF
    if pdf_type[pdf_type["image_found"]]:

        text = extract_scanned_pdf(pdf_path)

        save_txt(
            text,
            "PDFsCODE_output/scanned_pdf_chunk.txt"
        )

    # TABLE PDF

    if pdf_type["table_found"]:

        text = extract_table_pdf(pdf_path)

        save_txt(
            text,
            "PDFsCODE_output/table_pdf_chunk.txt"
        )

    if not (pdf_type["text_found"] and pdf_type["image_found"] and pdf_type["table_found"]):
        print("Unknown PDF Type")

pdf_path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\REC-BILL 2-1.pdf"

pdf_pipeline(pdf_path)