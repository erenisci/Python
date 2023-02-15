class employee:
    emp_num = 0
    pay_rate = 1.1

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        employee.emp_num += 1


print(employee.emp_num)
employee1 = employee("Eren", 51000)
print(employee.emp_num)
employee2 = employee("Selin", 50000)
print(employee.emp_num)

print(employee.pay_rate)
print(employee1.pay_rate)
print(employee2.pay_rate)

employee.pay_rate = 1.8
print(employee.pay_rate)
print(employee1.pay_rate)
print(employee2.pay_rate)

employee1.pay_rate = 2.1
print(employee.pay_rate)
print(employee1.pay_rate)
print(employee2.pay_rate)

employee.pay_rate = 1.2
print(employee.pay_rate)
print(employee1.pay_rate)
print(employee2.pay_rate)
