import time
import mechanicalsoup

browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)
# print(page.soup)

# browser = mechanicalsoup.Browser()
# page = browser.get("http://olympus.realpython.org/dice")
# tag = page.soup.select("#result")[0]
# result = tag.text

# print(f"The result of your dice roll is: {result}")

for i in range(1000):
    page = browser.get("http://olympus.realpython.org/dice")
    tag=page.soup.select('#result')[0]
    result=tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(1)