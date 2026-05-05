import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"(\w)\s+(\w)", r"\1\2", text)
    return text.strip()

text="""Dr. Jo hn Sm ith
MD"""
print(clean_text(text))