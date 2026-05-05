import re
import spacy











# # exercise 8
# nlp=spacy.load("en_core_web_sm")
# text="Contact Dr. John Smith at john.smith@gmail.com in India"
# doc=nlp(text)
# name=''
# location=''
# for i in doc.ents:
#     if i.label_ == "PERSON":
#         name=i.text
#     elif i.label_ == "GPE":
#         location=i.text
    
# pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# email=re.findall(pattern,text)
# result={
#     "Name":name,
#     "Email":email[0],
#     "Location":location
# }
# print(result)