name = "Eren"
tup = (1, 2, 3, 4)

for i in name:
    print(i)

for i in tup:
    print(i)

for sayi in range(11, 0, -1):
    print(sayi)

lst1 = ["a", "b", "c"]
lst2 = [1, 2, 3]

for char in lst1:
    for num in lst2:
        print(char, num)

for i in range(0, 11):
    if i % 2 == 0 and i != 6:
        print(i)
        continue
    elif i == 6:
        continue
    elif i == 9:
        break

a = 0
while a < 10:
    print(a)
    a += 1
