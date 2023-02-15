def take_pow(x):
    return x * x


lis = [1, 2, 4, 5, 7]
lis2 = []

for i in lis:
    lis2.append(take_pow(i))
print(lis2)


lis3 = map(take_pow, lis)
print(list(lis3))

lis4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis5 = list(map(lambda x: x * x, lis4))

lis6 = [1, 3, 4, 7, 8]
lis7 = [3, 5, 9, 8, 1]


def total(x, y):
    return x + y


res = list(map(total, lis6, lis7))
print(res)


products = [["Sneakers", 150], ["Trousers", 120], ["Shirt", 100], ["Jacket", 200]]


def discount(x):
    product, price = x[0], x[1]
    price = price * 0.9
    return [product, price]


res = list(map(discount, products))
print(res)

names = ["EreN", "aLiCe", "JaKe", "SelIn"]
res = list(map(lambda x: x.lower(), names))
print(res)

res = list(map(lambda x: x.title(), names))
print(res)
