def hello():
    print("Hello!")


hello()


def hello(isim):
    print("Hello! " + isim)


hello("Eren")


def summary(x, y):
    print(f"x + y = {x+y}")


summary(10, 5)


def product(x, y=15):
    print(f"x + y = {x*y}")


product(10)


def average(liste):
    summary = 0
    length = len(liste)
    for i in liste:
        summary += i
    return summary / length


liste = [1, 3, 5, 7, 9, 11]
result = average(liste)
print("Result:", result)
