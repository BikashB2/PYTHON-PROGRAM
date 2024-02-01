# Base class (parent class)
class Employee:
    def message(self):
        return "This is a general employee message."

# Child class 1
class Department(Employee):
    def message(self):
        return "This is a department-specific message."

# Child class 2
class Cells(Employee):
    def message(self):
        return "This is a cell-specific message."

# Create instances of the child classes
department_employee = Department()
cell_employee = Cells()

# Call the message method on instances
print(department_employee.message())  # Output: This is a department-specific message.
print(cell_employee.message())        # Output: This is a cell-specific message.
