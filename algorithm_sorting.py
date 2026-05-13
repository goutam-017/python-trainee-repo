data = [
    {"name": "Raj", "age": 25},
    {"name": "Amit", "age": 20},
    {"name": "Zara", "age": 30}
]
key = "age"
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][key] > data[j + 1][key]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)