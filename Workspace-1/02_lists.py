list = ["Black", "Red", "Yellow", "Orange", "Green"]

print(list[1:3])
print(list[::-1])
print(list)

list.append("White")
print(list)

list.insert(0, "Gray")

list.pop()
print(list)

list.pop(2)
print(list)

list.remove("Yellow")
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list_two = ["Red", "Yellow"]
list.extend(list_two)
print(list)

list.sort(reverse=True)
print(list)

list_three = sorted(list)
print(list_three)

string_colors = " ".join(list)
print(type(string_colors))
print(string_colors)

string_colors = string_colors.split(" ")
print(type(string_colors))
print(string_colors)

list_four = [1, 9, 3, 5, 7, 4, 8, 2, 6, 0]
print(list_four)
print(list_four.count(1))
print(list_four.index(0))
print(max(list_four))
print(min(list_four))
print(list_four[::-1])
print(sorted(list_four))

#####
# TEST
# string_list_four = ' '.join(map(lambda x: str(x), list_four))
# print(string_list_four)
