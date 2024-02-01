# Base class (parent class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Child class 1
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

# Child class 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

# Create instances of the child classes
student = Student("Alice", 18, "12345")
teacher = Teacher("Mr. Smith", 35, "Mathematics")

# Access attributes and methods from the parent and child classes
print(student.introduce())  # Output: My name is Alice and I am 18 years old.
print(student.study())      # Output: Alice is studying.

print(teacher.introduce())  # Output: My name is Mr. Smith and I am 35 years old.
print(teacher.teach())     # Output: Mr. Smith is teaching Mathematics.
