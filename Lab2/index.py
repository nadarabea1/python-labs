class Employee:
    employess = []

    def __init__(self, fisrt_name, last_name, age, department, salary):
        self.first_name = fisrt_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employess.append(self)

    def transfer(self, new_department):
        self.department = new_department

    def fire(self):
        Employee.employess.remove(self)

    def show(self):
        print(self.first_name, self.last_name,
              self.age, self.department, self.salary)

    def list_employees():
        for employee in Employee.employess:
            print(employee.first_name, employee.last_name)

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, Managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.Managed_department = Managed_department

    def show(self):
        print("Manager")
        super().show()
        print(self.Managed_department)


employees = []

while True:
    print("1. Add Employee (Enter 'add')")
    print("2. Add Manager (Enter 'm')")
    print("3. Show Employees (Enter 'list')")
    print("4. Quit (Enter 'q')")
    choice = input("Enter your choice: ")

    if choice == "add":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        employee = Employee(first_name, last_name, age, department, salary)
        employees.append(employee)
        print("Employee added successfully")

    elif choice == "m":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        Managed_department = input("Enter Managed department: ")
        manager = Manager(first_name, last_name, age,
                          department, salary, Managed_department)
        employees.append(manager)
        print("Manager added successfully")

    elif choice == "list":
        for employee in employees:
            employee.show()

    elif choice == "q":
        break

    else:
        print("Invalid choice")
