# def decorator(func):
#     def wrapper():
#         print("Operations before func runs")
#         func()
#         print("Operations after func runs")

#     return wrapper


# @decorator
# def func():
#     print("func running")


# func()

######
import time


def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"The process took {end - start} seconds")

    return wrapper


@calc_time
def take_pow(lis):
    for i in lis:
        print(i * i)


@calc_time
def take_cube(lis):
    for i in lis:
        print(i * i * i)


@calc_time
def add(a, b):
    time.sleep(1)
    print(a + b)


take_pow(range(100))
take_cube(range(100))
add(10, 20)
