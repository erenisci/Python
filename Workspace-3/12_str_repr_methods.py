class Footballer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"

    def __repr__(self):
        return f'Footballer("{self.name}", "{self.surname}", "{self.age}")'


footballer1 = Footballer("Eren", "Isci", 22)

# repr diye belirtmessek str basar
print(footballer1)
print(footballer1.__repr__)
