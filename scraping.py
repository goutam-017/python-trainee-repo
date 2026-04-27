from urllib.request import urlopen
import re

# url = "https://www.w3schools.com/python/default.asp"
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page=urlopen(url)
# html_bytes=page.read()
# html=html_bytes.decode("utf-8")
# print(html)
# title_index=re.findall('<title>',html)
# print(title_index)
# start_index = title_index + len("<title>")
# end_index=html.find('</title>')
# print(html[start_index:end_index])


# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# print(html)
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)


url="http://olympus.realpython.org/profiles/dionysus"
page=urlopen(url)
html=page.read().decode('utf-8')
pattern="<title.*?>.*?</title.*?>"
print(html)
match_result=re.search(pattern,html,re.IGNORECASE)
title=match_result.group()
title=re.sub("<.*?>", "", title)
print(title)