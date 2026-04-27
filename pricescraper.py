import mechanicalsoup
import time

url='https://books.toscrape.com/'
brower=mechanicalsoup.Browser()
page=brower.get(url)
soup=page.soup
books = soup.find_all("article", class_="product_pod")
print("This is a Book price Scraper Programming.")
print('\n')
for book in books:
    name=book.h3.a['title']
    price=book.find('p',class_='price_color').text
    print(name,":-",price)
    time.sleep(2)

print('\n')
print('Programm Ended......')