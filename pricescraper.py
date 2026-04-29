from groq import Groq
import mechanicalsoup
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
        print(f'{name}:- {price}')
        book_list.append([name,price])
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
            symbol=i[2][0]
            price=float(i[2].replace(symbol, ''))
            price_list.append(price)
            csv_data.append([book_name,i[2]])
    return price_list,csv_data,symbol
    

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
        price_list,csv_data,symbol=read_csv_file(file)
        result=get_price_calculation(price_list)
        print()
        print(f'Total price: {symbol}{result['total_price']}')
        print(f'Average price: {symbol}{result['average_price']}')
        print(f'Maximum price between all the books: {symbol}{result['maximum_price']}')
        print("\n")
        llm_price_calculation(csv_data)
    except Exception as e:
        print(f'Error is {e}')

def llm_price_calculation(csv_data):
    prompt="""
Analyze the CSV file with columns SN, Book Name, Price. Treat Price as numeric.

Tasks:
Total price sum
Average price
Highest-priced book (name + price)
Lowest-priced book (name + price)
Total number of books
Books above average price
Books below average price
Median price
Sorted price list
Currency Tasks:
Identify the currency symbol and its country/currency name
Convert all prices to Indian Rupees (INR) using the latest/provided exchange rate
Repeat the same analysis for INR prices
"""
    client=Groq(api_key=os.getenv("API_KEY"))
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role":"user","content":f'{csv_data},{prompt}'}],
        max_completion_tokens=8000
    )
    print(response.choices[0].message.content)

if __name__=='__main__':
    main(url)