def simplecalculator(a,s,b):
    try:
        symbol_list=['+', '-', '*', '/']
        if s in symbol_list:
            if(s=='+'):
                print(a+b)
            elif(s=='-'):
                print(a-b)
            elif(s=='*'):
                print(a*b)
            elif(s=='/'):
                print(a//b)
        else:
            print('Please enter a valid operation symbol..')
    except ZeroDivisionError:
        print('Error: Denominator cannot be 0.')

a=int(input('Enter the first number: '))
s=input('Enter which operation you want (+, -, *, /) : ')
b=int(input('Enter the second number: '))

simplecalculator(a,s,b)