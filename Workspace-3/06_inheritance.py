class Employee:
    pay_rate = 1.1

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name.lower() + surname.lower() + "@company.com"

    def info(self):
        return "Name: {}, Surname: {}, Salary: {}, Email: {}".format(
            self.name, self.surname, self.salary, self.email
        )


class Programmer(Employee):
    pay_rate = 1.2

    def __init__(self, name, surname, salary, lang):
        super().__init__(name, surname, salary)
        self.lang = lang

    def info(self):
        return "Name: {}, Surname: {}, Salary: {}, Email: {}, Language: {}".format(
            self.name, self.surname, self.salary, self.email, self.lang
        )

    def info_lang(self):
        return f"Language: {self.lang}"


employee1 = Employee("Eren", "Isci", 5000)
employee2 = Employee("Alice", "Parker", 4900)

programmer1 = Programmer("Selin", "Isci", 7000, "Python")
programmer2 = Programmer("John", "Hank", 8000, "Java")

print(employee1.pay_rate)
print(programmer1.pay_rate)

print(employee1.info())
print(employee2.info())

print(programmer1.info())
print(programmer2.info())

print(programmer1.info_lang())
