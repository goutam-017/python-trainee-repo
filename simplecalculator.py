def simplecalculator(a,s,b):
    try:
        symbol_list=['+', '-', '*', '/']
        if s in symbol_list:
            if(s=='+'):
                sum=a+b
                return f'Addition of two number is:{sum}'
            elif(s=='-'):
                sub=a-b
                return f'Substraction of two number is:{sub}'
            elif(s=='*'):
                mul=a*b
                return f'Multiplication of two number is:{mul}'
            elif(s=='/'):
                div=a//b
                return f'Division of two number is:{div}'
        else:
            return 'Please enter a valid operation symbol..'
    except ZeroDivisionError:
        return 'Error: Denominator cannot be 0.'

a=int(input('Enter the first number: '))
s=input('Enter which operation you want (+, -, *, /) : ')
b=int(input('Enter the second number: '))

print(simplecalculator(a,s,b))