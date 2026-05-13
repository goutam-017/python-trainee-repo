import pdfplumber
import fitz
import camelot
from pypdf import PdfReader

# pdf_path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\REC-BILL 2-1.pdf"

def detect_pdf_type(pdf_path):

    result = {
        "encrypted": False,
        "text_pdf": False,
        "scanned_pdf": False,
        "hybrid_pdf": False,
        "table_pdf": False,
        "contains_images": False
    }

    # 1. Check Encrypted PDF
    reader = PdfReader(pdf_path)

    if reader.is_encrypted:
        result["encrypted"] = True
        return result

    # 2. Check Text Extraction
    text_found = False

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text and text.strip():
                text_found = True
                break

    #Check Images
    image_found = False

    doc = fitz.open(pdf_path)

    for page in doc:

        images = page.get_images()

        if len(images) > 0:
            image_found = True
            break

    #Detect PDF Type
    if text_found and image_found:
        result["hybrid_pdf"] = True

    elif text_found:
        result["text_pdf"] = True

    elif image_found:
        result["scanned_pdf"] = True

    result["contains_images"] = image_found

    #Detect Tables
    try:

        tables = camelot.read_pdf(
            pdf_path,
            pages="1",
            flavor="stream"
        )

        if tables.n > 0:
            result["table_pdf"] = True

    except:
        pass

    return result
