def simplecalculator(a,s,b):
    try:
        symbol_list=['+', '-', '*', '/']
        if s in symbol_list:
            if(s=='+'):
                sum=a+b
                return sum
            elif(s=='-'):
                sub=a-b
                return sub
            elif(s=='*'):
                mul=a*b
                return mul
            elif(s=='/'):
                div=a//b
                return div
        else:
            return 'Please enter a valid operation symbol..'
    except ZeroDivisionError:
        return 'Error: Denominator cannot be 0.'

a=int(input('Enter the first number: '))
s=input('Enter which operation you want (+, -, *, /) : ')
b=int(input('Enter the second number: '))

print(simplecalculator(a,s,b))