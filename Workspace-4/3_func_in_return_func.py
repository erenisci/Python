def pick_process(process):
    def addition(*args):
        return sum(args)

    def multiplication(*args):
        product = 1
        for arg in args:
            product *= arg
        return product

    def average(*args):
        return sum(args) / len(args)

    if process == "Addition":
        return addition
    elif process == "Multiplication":
        return multiplication
    elif process == "Average":
        return average


my_func = pick_process("Addition")
print(my_func(2, 3, 4, 5, 6))


#####
def pick_person(person):
    def pick_team(team):
        return f"{person} {team}"

    return pick_team


a = pick_person("Eren")
b = pick_person("Alice")

print(a("Fenerbahce"))
print(b("Samsunspor"))
