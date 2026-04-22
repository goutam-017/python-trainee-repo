def simplecalculator(a,s,b):
    try:
        symbol_list=['+', '-', '*', '/']
        if s in symbol_list:
            if(s=='+'):
                sum=a+b
                return f'Addition of two number is: {sum}'
            elif(s=='-'):
                sub=a-b
                return f'Substraction of two number is: {sub}'
            elif(s=='*'):
                mul=a*b
                return f'Multiplication of two number is: {mul}'
            elif(s=='/'):
                if((type(a)==float and type(b)==float) or (type(a)==float and type(b)==int) or (type(a)==int and type(b)==float)):
                    div=a/b
                else:
                    div=a//b
                return f'Division of two number is: {div}'
        else:
            return 'Please enter a valid operation symbol..'
    except ZeroDivisionError:
        return 'Error: Denominator cannot be 0.'

a=eval(input('Enter the first number: '))
b=eval(input('Enter the second number: '))
s=input('Enter which operation you want (+, -, *, /) : ')
print(simplecalculator(a,s,b))