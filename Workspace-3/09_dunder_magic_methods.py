class Footballer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __add__(self, other):
        name = self.name[:2] + other.name[0:2].lower()
        surname = (
            self.surname[: int(len(self.surname) / 2)]
            + other.surname[int(len(other.surname) / 2) :]
        )
        age = round(self.age + other.age / 2)
        return Footballer(name, surname, age)

    def __eq__(self, other):  # To get called on comparison using == operator.
        if self.name == other.name and self.surname == other.surname:
            return True
        return False

    def __lt__(self, other):  # To get called on comparison using < operator.
        if self.age < other.age:
            return True
        return False

    def __gt__(self, other):  # To get called on comparison using > operator.
        if self.age > other.age:
            return True
        return False


footballer1 = Footballer("Eren", "Isci", 22)
footballer2 = Footballer("Alice", "Parker", 21)

footballer3 = footballer1 + footballer2
print(footballer3.name)
print(footballer3.surname)
print(footballer3.age)

print(footballer1 == footballer2)
print(footballer1 > footballer2)
print(footballer1 < footballer2)
