l = [[1], [1, 1]]
n = 8

# n = int(input("How many levels would you like to see from pascal's triangle? : "))
# print()

for i in range(2, n + 1):
    element = []
    for j in range(0, i + 1):
        if j == 0 or j == i:
            element.append(1)
        else:
            element.append(l[i - 1][j - 1] + l[i - 1][j])
    l.append(element)

i = n
with open(
    "Python\\Projects\\3-Pascal-Triangle\\pascal.txt",  # -> with open("location", "w") as f:
    "w",
) as f:
    for index in l:
        index = " ".join(str(i) for i in index)
        f.write(
            f"{index:^{n*6}} --> level = {n - i}, sum of numbers = {2 ** (n - i)}\n"
        )
        i -= 1
