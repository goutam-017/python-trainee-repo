import pdfplumber

path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\medical_report1.pdf"
# with pdfplumber.open(path) as pdf:
#     for page in pdf.pages:
#         print(page.extract_text())

with pdfplumber.open(path) as pdf:
    for page_num,page in enumerate(pdf.pages):
        print(page_num,page.extract_text())