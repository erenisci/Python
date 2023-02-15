class employee:
    def __init__(self, name="not found", surname="not found", age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}")


employee1 = employee()
employee2 = employee("Eren", "Isci", 22)
employee3 = employee(age=17, name="Selin", surname="Isci")

employee1.show_info()
employee2.show_info()
employee3.show_info()
