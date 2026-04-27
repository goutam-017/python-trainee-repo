import re


s='abhgtfyc'
p='a.*c'
o=re.findall(p,s)
print(o)

string = "Everything is <replaced> if it's in <tags>."
s=re.sub("<.*?>",'Elephants',string)
print(s)