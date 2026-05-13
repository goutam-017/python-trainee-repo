from paddleocr import PaddleOCR
from pdf2image import convert_from_path


ocr = PaddleOCR(use_angle_cls=True, lang='en')


def extract_text(pdf_path):

    full_text = ""

    images = convert_from_path(
        pdf_path,
        dpi=300
    )

    for img in images:

        result = ocr.ocr(img)

        for line in result[0]:

            text = line[1][0]

            full_text += text + "\n"

    return full_text


text = extract_text("sample.pdf")

print(text)