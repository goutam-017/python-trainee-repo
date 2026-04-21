l=[1,2,3,4,5,6]

p=[num*2 for num in l]
print(p)

even_number=[num for num in range(1,11) if num%2 == 0]
print(even_number)

numbers=[1, 2, 3, 4, 5, 6]
even_odd_list=["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(even_odd_list)

result=[[i*j for j in range(2,6)] for i in range(1,5)]
print(result)