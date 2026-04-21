import csv


# with open('file.txt','r') as file1:
#     read_file=file1.read()
#     print(read_file)


with open('file2.txt','w') as file2:
    file2.write('Python programming is fun. \n')
    file2.write('I really enjoy writing programming in Python. \n')

with open('file2.txt','r') as file2:
    read_file=file2.read()
    print(read_file)


# with open('people.csv','r') as file:
#     read=csv.reader(file)

#     for row in read:
#         print(row)

# with open('file1.csv','w',newline='') as file:
#     write=csv.writer(file)
#     write.writerow(['SN','Movie','Protagonist'])
#     write.writerow([1,'Lord of the Rings','Froda Baggins'])

# with open('file1.csv','r') as file:
#     read=csv.reader(file)
#     for row in read:
#         print(row)