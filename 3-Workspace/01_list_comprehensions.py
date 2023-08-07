# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list = []
for number in numbers:
    list.append(number)
print(list)

list2 = [number for number in numbers]
print(list2)


# 2
list = []
for number in numbers:
    if number % 2 == 0:
        list.append(number)
print(list)

list2 = [number for number in numbers if number % 2 == 0]
print(list2)


# 3
list = []
for number in numbers:
    if number % 2 == 0:
        list.append(number**2)
print(list)

list2 = [number**2 for number in numbers if number % 2 == 0]
print(list2)


# 4
list = []
for number in numbers:
    if number > 4 and number % 2 == 0:
        list.append(number**2)
print(list)

list2 = [number**2 for number in numbers if number > 4 and number % 2 == 0]
print(list2)


# 5
numbers = [1, 2, 3, 4]
letters = "abcd"

list = []
for number in numbers:
    for letter in letters:
        list.append((number, letter))
print(list)

list2 = [(number, letter) for number in numbers for letter in letters]
print(list2)


# 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [2, 3, 6, 9, 5]

list = []
for i in numbers:
    if i not in numbers2:
        list.append(i * i)
print(list)

list2 = [i * i for i in numbers if i not in numbers2]
print(list2)


# 7
liste = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
list = []
for i in liste:
    for j in i:
        list.append(j)
print(list)

list2 = [j for i in liste for j in i]
print(list2)


# 8
list_methods = []
for method in dir(list):
    if method.startswith("__"):
        continue
    list_methods.append(method)
print(list_methods)

list2 = [method for method in dir(list) if not method.startswith("__")]
print(list2)
