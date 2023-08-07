class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name_surname(self):
        return f"{self.name} {self.surname}"

    def email(self):
        return f"{self.name.lower()}.{self.surname.lower()}@company.com"

    @name_surname.setter
    def name_surname(self, name):
        name, surname = name.split(" ")
        self.name = name
        self.surname = surname

    @name_surname.deleter
    def name_surname(self):
        print("Deleted!")
        self.name = None
        self.surname = None


person1 = Person("Eren", "Isci")
print(person1.name)
print(person1.name_surname)
print(person1.email())
print()

person2 = Person("Alice", "Parker")
print(person2.name_surname)
print()

person2.name_surname = "John Hank"
print(person2.name_surname)
print(person2.email())
print()

del person1.name_surname
del person2.name_surname
print()

print(person1.name_surname)
print(person2.name_surname)
