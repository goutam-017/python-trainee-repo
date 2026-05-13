import os
import fitz

# g = (i for i in range(3))

# print(list(g))
# print(list(g))
# print(type(g))

# print(os.path.exists(r"C:\poppler\Library\bin"))

# s="hello\\nworld"
# print(s)
# print(s.replace('\\n'," "))


pdf_path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\REC-BILL 2-1.pdf"
doc = fitz.open(pdf_path)

for page in doc:

    images = page.get_images()
    print(images)

    # if len(images) > 0:
    #     image_found = True
    #     break