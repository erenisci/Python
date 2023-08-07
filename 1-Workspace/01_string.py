var = "Hello"
var_two = "World!"

print(var + " World!")
print((var + " World!").lower())
print((var + " World!").upper())
print((var + " World!").capitalize())
print((var + " World!").startswith(("H").lower()))
print((var + " World!").replace("World!", "Beauty ;)"))
print((var + " " + var_two).swapcase())
print(var.replace("o", "aaa"))
print("     AaBbCc     ".strip())
print(len("Software"))


new_string = var.lower() + " World!".lower()
print(new_string)

new_string = new_string.title()
print(new_string)


print(var[-2])
print(var[0])
print(var[0:4:2])
print(var[::-1])
print(var[::-1] * 3)
print(var[::2])


print("{} {}".format(var, var_two))
print("{a} {b}".format(a=var, b=var_two))
print("{b} {a}".format(a=var, b=var_two))
print("{a} {b}".format(b=var, a=var_two))


var_three = 21
var_four = 21.2199999

print("A =", 21)
print("A =", var_three)
print("A = %d" % var_three)
print("var = %s" % var)
print("var_four = %.2f" % var_four)
print("var = %s, var_three = %d, var_four = %.2f" % (var, var_three, var_four))


# or name, age, job = 'Eren', 21, 'Software Engineer'
name = "Eren"
age = 21
job = "Software Engineer"

print("My name is {name}, age is {age} and i am a {job}")
print(f"My name is {name}, age is {age} and i am a {job}")
print(f"{var:^{30}}{'VS':^{15}}{var_two:^{30}}")


print(*"Hello World", sep="\n")
