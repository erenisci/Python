take_pow = lambda x: x * x
print(take_pow)
print(take_pow(5))

take_cube = lambda x: x**3
print(take_cube)
print(take_cube(5))

res = lambda x, y: x + y
print(res)
print(res(5, 8))

total = lambda *args: sum(args)
print(total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print((lambda x, y, z: x * y + z)(3, 5, 6))
print((lambda *args: sum(args) / len(args))(2, 4, 6, 8, 10))

lis = [("Zeynep", 21), ("Alice", 20), ("Eren", 22), ("Selin", 31)]
print(sorted(lis))

lis.sort(key=lambda x: x[1])
print(lis)

lis2 = [
    {"Name": "Eren", "Surname": "Isci", "Age": 22},
    {"Name": "Zeynep", "Surname": "Yilmaz", "Age": 21},
    {"Name": "Selin", "Surname": "Isci", "Age": 17},
    {"Name": "Alice", "Surname": "Parker", "Age": 31},
]
lis2.sort(key=lambda x: x["Surname"])
for dic in lis2:
    print(dic["Surname"])

lis2.sort(key=lambda x: x["Age"])
print(lis2)
