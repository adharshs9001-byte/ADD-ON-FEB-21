class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by {amount}. New salary: {self.salary}")
        else:
            print("Increase amount must be positive.")

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


# Example usage
emp1 = Employee("Abhinav", "EMP101", 35000)

emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()