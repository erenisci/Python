with open("Workspace-2\project_input.txt", "r") as file:
    lines = file.read().splitlines()
    lines.pop(0)

list = []
for line in lines:
    list_line = []
    name_surname = line.split()[0]
    surname = name_surname.split("-")[-1]

    name = name_surname[: name_surname.index(surname) - 1]
    name = name.replace("-", " ")
    list_line.append(name)
    list_line.append(surname)

    job = ""
    indexes = []
    for i in range(len(line)):
        if line[i] == " ":
            indexes.append(i)
    job = line[indexes[0] : indexes[-1]]
    list_line.append(job)

    notes = line.split()[-1]
    midterm = int(notes.split("/")[0])
    midterm_two = int(notes.split("/")[1])
    final = int(notes.split("/")[2])
    average = midterm * 0.3 + midterm_two * 0.3 + final * 0.4  #
    average = str(average)
    list_line.append(average[:4])
    list.append(list_line)

titles = ["NAME", "SURNAME", " JOB", "AVERAGE"]
list.insert(0, titles)

with open("Workspace-2\project_output.txt", "w") as file:
    last_line = len(list)
    for index in list:
        if index == list[1]:
            file.write("\n")
        if index == list[last_line - 1]:
            file.write(f"{index[0]:<30}{index[1]:<30}{index[2]:<30}{index[3]}")
        else:
            file.write(f"{index[0]:<30}{index[1]:<30}{index[2]:<30}{index[3]}\n")
