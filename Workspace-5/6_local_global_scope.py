x = "global x"


def func1():
    x = "local x"
    print(x)


func1()
print(x)

print("\n***************\n")
#####

y = "global y"


def outer():
    y = "enclosing y"
    print(y)

    def inner():
        y = "local y"
        print(y)

    inner()


outer()
print(y)

print("\n***************\n")
#####

x = "global x"


def func2():
    global x
    x = 5


func2()
print(x)

print("\n***************\n")
#####

y = "global y"


def outer():
    y = "enclosing y"
    print(y)

    def inner():
        nonlocal y
        y = 5

    inner()
    print(y)


outer()
print(y)
