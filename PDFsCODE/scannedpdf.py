import spacy
import pdfplumber,camelot,warnings,re,os
import pandas as pd
from pdf_detect import detect_pdf_type

pdf_path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\REC-BILL 2-1.pdf"
pattern_date=[r"\d{1,2}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{4}",
              r"\d{4}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{1,2}",
              r"[A-Za-z]{3}\s*\d{1,2}\s*[,]\s*\d{4}",]


date_types = {
    "DOB": "Date of Birth",
    "DOS": "Date of Service",
    "Performed Date": "Performed Date",
    "Date of Study": "Study Date",
    "Date of Read": "Read Date",
    "Generated": "Generated Date",
    "signed": "Signed Date",
    "Onset": "Onset Date",
    "Appointment": "Appointment Date"
}

def extract_normal_text(pdf_path):
    text=""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()

    return text

# using pdfplumber
def extract_all_table_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:

                df = pd.DataFrame(table)

                text += df.to_string(index=False)
                text += "\n\n"

    return text

print(extract_all_table_text(pdf_path))

# # using camelot
# def extract_all_table_text(path):
#     warnings.filterwarnings("ignore")
#     tables = camelot.read_pdf(path, pages="all", flavor="stream")  
#     all_tables_text = []

#     for table in tables:
#         df = table.df  
#         text = " ".join(
#             " ".join(str(cell) for cell in row)
#             for row in df.values
#         )
#         all_tables_text.append(text)

#     table_txt = " ".join(all_tables_text)
#     return table_txt

# text=extract_all_table_text(pdf_path)+extract_normal_text(pdf_path)

# file_path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\table_text.txt"
# with open(file_path,'w',encoding='utf-8') as a:
#     a.write(text)

# all_dates=[]
# for p in pattern_date:
#     dates=re.findall(p,text)
#     all_dates.extend(dates)
 
# print(set(all_dates))


# text="Patient was seen by Dr. John Smith and nurse Jane Doe."

# path=r"C:\Users\hp\Desktop\Python Training\PDFsCODE\table_text.txt"

# with open(file_path,'r',encoding='utf-8') as file:
#     read_text=file.read()

# nlp = spacy.load("en_core_web_sm")

# def extract_names_ner(text):
#     doc = nlp(text)
#     out=[]
#     for ent in doc.ents:
#         if ent.label_ == 'PERSON':
#             out.append(ent.text)
#     return out
# def extract_date_ner(text):
#     doc = nlp(text)
#     out=[]
#     for ent in doc.ents:
#         if ent.label_ == 'DATE':
#             out.append(ent.text)
#     return out


# extract_date_ner(read_text)