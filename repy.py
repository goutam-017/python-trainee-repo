import re


s='abhgtfyc'
p='a.*c'
o=re.findall(p,s)
print(o)

string = "Everything is <replaced> if it's in <tags>."
s=re.sub("<.*?>",'Elephants',string)
print(s)

with open("raw/chunk_0001.txt",'r') as f:
    text=f.read()

pattern_date=[r"\d{1,2}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{4}",
              r"\d{4}\s*[/-]\s*\d{1,2}\s*[/-]\s*\d{1,2}"]

dates=[]
for p in pattern_date:
    d=re.findall(p,text)
    dates.extend(d)

for d in dates:
    print(d)