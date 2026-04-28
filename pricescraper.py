from groq import Groq
import mechanicalsoup
import time
import csv
import os

url='https://books.toscrape.com/'


def web_scraper(url):
    browser=mechanicalsoup.Browser()
    page=browser.get(url)
    soup=page.soup
    books = soup.find_all("article", class_="product_pod")
    print("This is a Book price Scraper Programming.")
    print()
    book_list=[]
    for book in books:
        name=book.h3.a['title']
        price=book.find('p',class_='price_color').text
        print(name,":-",price)
        book_list.append([name,price])
        # time.sleep(2)
    return book_list

def create_csv_file(book_list,file):
    with open(file,'w',newline='') as a:
        write=csv.writer(a)
        write.writerow(['SN','Book Name','price'])
        j=1
        for i in book_list:
            price = i[1]
            write.writerow([j,i[0],price])
            j+=1
    return file


def read_csv_file(file):
    price_list=[]
    csv_data=[]
    with open(file,'r',encoding='cp1252') as f:
        read=csv.reader(f)
        next(read)
        for i in read:
            book_name=i[1]
            price=float(i[2].replace('£', ''))
            price_list.append(price)
            csv_data.append([book_name,i[2]])
    return price_list,csv_data
    

def get_price_calculation(price_list):
    total_price=0
    maximum_price=max(price_list)
    for i in price_list:
        price=float(i)
        total_price+=price
    average_price=total_price//len(price_list)
    return {
        "total_price":total_price,
        "average_price":float(average_price),
        "maximum_price":maximum_price
    }

def main(url):
    try:
        book_list=web_scraper(url)
        file=create_csv_file(book_list,'price.csv')
        price_list,csv_data=read_csv_file(file)
        result=get_price_calculation(price_list)
        print()
        print(f'Total price: £{result['total_price']}')
        print(f'Average price: £{result['average_price']}')
        print(f'Maximum price between all the books: £{result['maximum_price']}')
        print("\n")
        llm_price_calculation(csv_data)
    except Exception as e:
        print(f'Error is {e}')

def llm_price_calculation(csv_data):
    prompt="""
Analyze the provided CSV dataset containing book data with columns SN, Book Name, Price. Treat the Price column as numeric values. Perform complete data analysis and calculations based only on the CSV data.

Tasks to perform:
Calculate the total sum of all book prices.
Calculate the average (mean) price.
Find the highest priced book with its name and price.
Find the lowest priced book with its name and price.
Count the total number of books.
Show books with price above average.
Show books with price below average.
If needed, calculate median price and sorted price list.

Return the result in a clean, structured format with labels. Use accurate mathematical calculations.
"""
    client=Groq(api_key=os.getenv("API_KEY"))
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":f'{csv_data},{prompt}'}],
    )
    print(response.choices[0].message.content)

if __name__=='__main__':
    main(url)