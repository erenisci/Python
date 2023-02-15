def outer():
    print("outer func start")

    def inner():
        print("inner func")

    print("outer func end")
    inner()


outer()


#####
def calculate(x):
    def take_pow(a):
        return a**2

    def take_sqrt(a):
        return a**0.5

    def take_factorial(a):
        product = 1
        for i in range(1, a + 1):
            product *= i
        return product

    a = take_pow(x)
    b = take_sqrt(x)
    c = take_factorial(x)
    return f"Pow: {a}, Sqrt: {b}, Factorial: {c}"


print(calculate(6))
