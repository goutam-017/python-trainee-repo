import datetime

now=datetime.datetime.now()
print(now)

date=datetime.date.today()

day=date.day
month=date.month
year=date.year
print(f'{day}.{month}.{year}')