def take_pow(x, y):
    return x**y


print(take_pow(3, 4))


#
def info(name, surname="None", age="None"):
    return f"name: {name}, surname: {surname}, age: {age}"


print(info("Alice"))


#
def info2(name="None", surname="None", age="None"):
    return f"name: {name}, surname: {surname}, age: {age}"


print(info2("Alice", age=21))
print(info2())


#
def addition1(x, y):
    return x + y


def addition2(x, y, z):
    return x + y + z


def addition(*args):
    for arg in args:
        print(arg)


addition(1, 2, 3, 4, 5, "Python", True)


#
def multiplication(*args):
    product = 1
    for arg in args:
        product *= arg

    print("Product:", product)


multiplication(3, 4)


#
def average(*args):
    return sum(args) / len(args)


print(average(2, 3, 4, 5, 6))


#
def say_hi(mesaj, *args):
    res = ""
    res += mesaj + " "
    for arg in args:
        res += arg + " "
    return res


print(say_hi("Hello", "Eren", "How are you?"))


#
def func1(**kwargs):
    print(kwargs)


func1(name="Eren", surname="Isci", age=22)


#
def func2(first, *args, **kwargs):
    print(first)
    print("********")
    for arg in args:
        print(arg)
    print("********")
    for k, v in kwargs.items():
        print(k + ":", v)


func2(2, 3, 4, 5, 6, 7, name="Eren", age=22)
