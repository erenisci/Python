from functools import reduce
from math import gcd


lis = [2, 4, 6, 9]


def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


res1 = reduce(addition, lis)
print(res1)
res2 = reduce(multiplication, lis)
print(res2)


def lcd(x, y):
    return int((x * y) / gcd(x, y))


reslcd = reduce(lcd, lis)
print(reslcd)


def rock_paper_scissors(x, y):
    s = {x, y}
    if x == y:
        return x
    if s == {"rock", "scissors"}:
        return "rock"
    if s == {"rock", "paper"}:
        return "paper"
    if s == {"paper", "scissors"}:
        return "scissors"


lis2 = ["rock", "paper", "rock", "scissors", "paper", "scissors", "rock"]
res3 = reduce(rock_paper_scissors, lis2)
print(res3)
