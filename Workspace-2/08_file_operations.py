# file = open('test.txt', 'w')
# text = 'Python'
# file.write(text)
# file.close

with open("Workspace-2\\test.txt", "w") as file:
    text = "Python"
    file.write(text)

# file = open('test.txt', 'r')
# text = file.read()
# print(text)
# file.close()

with open("Workspace-2\\test.txt", "r") as file:
    text = file.read()
    print(text)
