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


class Manager(Employee):
    def __init__(self, name, surname, salary, worker=None):
        super().__init__(name, surname, salary)
        if worker == None:
            self.worker = []
        else:
            self.worker = worker

    def add_worker(self, worker):
        if worker not in self.worker:
            self.worker.append(worker)

    def del_worker(self, worker):
        if worker in self.worker:
            self.worker.remove(worker)

    def show_worker(self):
        for worker in self.worker:
            print(worker.info())


employee1 = Employee("Eren", "Isci", 5000)
employee2 = Employee("Alice", "Parker", 4900)

programmer1 = Programmer("Selin", "Isci", 7000, "Python")
programmer2 = Programmer("John", "Hank", 8000, "Java")

manager1 = Manager("Steve", "Johnson", 10000)

print("\n*************************")
manager1.add_worker(programmer1)
manager1.add_worker(programmer2)
manager1.show_worker()

print("\n*************************")
manager1.del_worker(programmer1)
manager1.show_worker()

print("\n*************************")
print(isinstance(manager1, Manager))
manager2 = Manager("Tim", "Rogers", 10000, [manager1])
manager2.show_worker()

print("\n*************************")
print(isinstance(manager1, Employee))
print(isinstance(manager1, Manager))

print("\n*************************")
print(issubclass(Programmer, Employee))
print(issubclass(Employee, Programmer))
