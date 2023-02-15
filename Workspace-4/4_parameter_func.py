def take_pow(x):
    return x * x


def take_cube(x):
    return x**3


def map_func(func, lis):
    res = []
    for i in lis:
        res.append(func(i))
    return res


lis1 = [1, 2, 3, 4, 5]
lis2 = [1, 3, 4, 5, 8, 9, 11]


print(map_func(take_pow, lis1))
print(map_func(take_cube, lis2))
