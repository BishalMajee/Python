# Define the Person class
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")

# Define the Employee class that inherits from Person
class Employee(Person):
    def __init__(self, name, gender, age, employee_id, department, salary):
        # Initialize the Person part
        super().__init__(name, gender, age)
        # Initialize the Employee part
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    
    def print_details(self):
        # Print the details from the Person class
        super().print_details()
        # Print the additional details from the Employee class
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

# Create an Employee object, initialize it, and print its details
employee = Employee("Bishal", "Male", 21, "A125", "Data Analyst", 100000)
employee.print_details()
