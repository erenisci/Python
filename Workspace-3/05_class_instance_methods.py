from datetime import date


class Person:
    person_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_count += 1

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

    @classmethod
    def person_counter(cls):
        return cls.person_count

    @classmethod
    def create_string(cls, str_):
        name, age = str_.split("-")
        return cls(name, age)

    @classmethod
    def create_birthday(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    @staticmethod
    def calculate_birthyear(Person):
        return date.today().year - Person.age


person1 = Person("Eren", 20)
person2 = Person("Selin", 30)
person3 = Person.create_string("John-25")
person4 = Person.create_birthday("Alice", 2001)

print(Person.person_counter())

print(Person.calculate_birthyear(person1))
