class Job():
    def __init__(self, title, company, salary):
        self.title = title
        self.company = company
        self.salary = salary

    def display_info(self):
        print(f"Job Title: {self.title}")
        print(f"Company: {self.company}")
        print(f"Salary: ${self.salary}")

class Employee(Job):
    def __init__(self, title, company, salary, name, age):
        super().__init__(title, company, salary)
        self.name = name
        self.age = age

    def display_info(self):
        super().display_info()
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")

class Manager(Employee):
    def __init__(self, title, company, salary, name, age, department):
        super().__init__(title, company, salary, name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
