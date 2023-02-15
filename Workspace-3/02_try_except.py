try:
    a = 5
    b = 0
    # if b == 0:
    #     raise ZeroDivisionError
    c = a / b
    x = 4
    d = x
    name = "Eren"
    char = name[0]
except ZeroDivisionError as error:
    print("Zero Division Error!,", error)
except NameError:
    print("Name Error!")
except IndexError:
    print("Index Error!")
except Exception:
    print("Unknown Error!")
else:
    print("Else block is working!")
finally:
    print("Finally block is working!")
