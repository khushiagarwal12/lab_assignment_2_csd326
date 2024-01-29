class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def sort_by_age(self):
        self.employees.sort(key=lambda x: x.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda x: x.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda x: x.salary)

    def print_table(self):
        for emp in self.employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

# Sample data
employee_table = EmployeeTable()
employee_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
employee_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
employee_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
employee_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

# Sorting based on user choice
choice = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
if choice == 1:
    employee_table.sort_by_age()
elif choice == 2:
    employee_table.sort_by_name()
elif choice == 3:
    employee_table.sort_by_salary()

# Printing sorted table
print("Sorted Employee Table:")
employee_table.print_table()
