import mechanicalsoup
import time

url='https://web-scraping.dev/products'
browser=mechanicalsoup.Browser()
page=browser.get(url)
soup=page.soup
tag=soup.select('title')[0]
result=tag.text
print(result)
print('\n')
products=soup.select('.product')
for p in products:
    name=p.select_one('h3').text
    price=p.select_one('.price').text
    print(name,':-',price)
    time.sleep(2)