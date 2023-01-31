a = 5
b = 8
c = 10

if a < b and b == c:
    print("True")
else:
    print("False")

lst = [1, 2, 3, 4, 5, 6, 7]

if a in lst:
    print("in list")
else:
    print("not in list")

name = "Python"
c = "P"
if c in name:
    print("in list")
else:
    print("not in list")


a = "python"
b = "pytho"
b += "n"
print(a, b, sep="\n")
if a is b:  # Memory
    print("a = b")
else:
    print("a != b")
    print(id(a))
    print(id(b))
