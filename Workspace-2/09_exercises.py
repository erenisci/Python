import random
import time


def exercise(n):
    list = []
    for i in range(n + 1):
        list.append([random.randint(1, 30), time.strftime("%S")])  # S (second)
        time.sleep(0.31)
    list.pop(0)
    return list


n = int(input())
list = exercise(n)
print(list)
