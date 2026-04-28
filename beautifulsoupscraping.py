from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://books.toscrape.com/'
page=urlopen(url)
html=page.read().decode('utf-8')
soup=BeautifulSoup(html,'html.parser')
print(soup.get_text())
print(soup.find_all('img'))
img1,img2=soup.find_all('img')
print(img1['src'])
print(img2['src'])
print(soup.title.text)
print(soup)