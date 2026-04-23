name=input('Enter a Name:')

print(name)

def hello(first_name,last_name):
    print('First Name: ',first_name)
    print('Last Name: ',last_name)

hello(last_name='Senapati',first_name='Goutam')

msg='Hello world'
def greet():
    print(msg,'in local')

print(msg,'in global')
greet()

a=[1,2,3,4]
def hello(a):
    a.append(4)
    print(a)
hello(a)    
print(a)


functions = []

for i in range(4):
    functions.append(lambda j=i: j)
print(type(functions))
print(type(functions[0]))
print(functions[0]())
for f in functions:
    print(f())


a='goutam'
b='goutam'
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))

print(a == b)
print(a is b)

nums = [x*x for x in range(5)]
gen = (x*x for x in range(5))
print(nums)
print(gen)