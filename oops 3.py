# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden by child classes

# Derived class (child class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (child class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on the instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
