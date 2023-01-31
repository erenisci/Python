list = ["Name", "Age", "School_ID", "Phone_Num", "Height_Meter"]
my_dict = {}

for key in list:
    if key == "Name":
        my_dict[key] = input(key + ": ")
    elif key == "Height_Meter":
        my_dict[key] = float(input(key + ": "))
    else:
        my_dict[key] = int(input(key + ": "))

print("\nPerson info: ")
for key, value in my_dict.items():
    print(" " + key + ": " + str(value))


# Turkish baklava with digit of age (???)(Training :)
for i in range(my_dict["Age"]):
    for j in range(my_dict["Age"] - i):
        print(" ", end="")
    for k in range(i - 1):
        print(my_dict["Age"], end="")
    print()

for i in range(my_dict["Age"]):
    for k in range(i):
        print(" ", end="")
    for j in range(my_dict["Age"] - i - 1):
        print(my_dict["Age"], end="")
    print()
