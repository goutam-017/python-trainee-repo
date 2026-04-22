import re

greeting=lambda name: print(f'Hello {name}')
greeting('Goutam')

# iterator
my_list=[1,2,3,4,5]

iterator=iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in iterator:
    print(i)

# Generator
l=[1, 2, 3]
def func(s):
    yield s[0]
    yield s[1]
    yield s[2]
gen=func(l)

print(next(gen))
print(next(gen))
print(next(gen))

def my_generator(n):
    value=1
    while value<=n:
        yield value
        value+=1

for i in my_generator(5):
    print(i)

generator=(i*i for i in range(6))
for i in generator:
    print(i)

print(type(generator))


def fibonacci_number(n):
    x,y=0,1
    for _ in range(n):
        x,y=y,x+y
        yield x

def square(n):
    for i in n:
        yield i**2

print(sum(square(fibonacci_number(10))))

def greeting(name):
    def innner():
        return 'Hello '+name
    return innner()
print(greeting('Goutam'))

def greet():
    name='Goutam'
    return lambda : 'hii '+name

msg=greet()
print(msg())

def outer(x):
    def inner(y):
        print(x)
        print(y)
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)



# decorator
def make_pretty(func):
    def inner():
        print('i got decorated.')
        func()
    return inner

@make_pretty
def ordinary():
    print('i am ordinary')

ordinary()

pattern='^a..b$'
string='aysb'
result=re.match(pattern,string)
if result:
    print('pattern match successfully.')
else:
    print("pattern doesn't match.")