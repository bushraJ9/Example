class Person:
    def show_info(self):
        pass


class Employee(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


    def show_info(self):
        return f"Employee: {self.name}, Age: {self.age}, Dept: {self.department}"


class Manager(Employee):
    def __init__(self, name, age, department, team_size):
        super().__init__(name, age, department)
        self.team_size = team_size

    def show_info(self):
        return f"Manager: {self.name}, Age: {self.age}, Department: {self.department}, Team Size: {self.team_size}"


Employee1 = Employee("Rahaf", 24, "SOC L1")
Manager1 = Manager("Bushra", 24, "SOC Leader", 5)

print(Employee1.show_info())
print(Manager1.show_info())
