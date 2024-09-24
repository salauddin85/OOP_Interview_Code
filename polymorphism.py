# Polymorphism is one of the core concepts of Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It means "many shapes" and allows methods to do different things based on the object that it is acting upon, even if they share the same name.

# There are two main types of polymorphism in Python:

# Compile-Time Polymorphism (Static Polymorphism)
# Run-Time Polymorphism (Dynamic Polymorphism)



# Runtime Polymorphism -> Dynamic Binding | Overriding | Late Binding

# CompileTime Polymorphism-> Static Binding | Overloading | Early Binding

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())




# 1. Compile-Time Polymorphism (Static Polymorphism)
# In Python, compile-time polymorphism is typically achieved through method overloading. This allows multiple methods with the same name to exist in the same scope but with different parameters (though Python does not support method overloading in the same way as languages like C++ or Java).

# Example (Method Overloading):

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c  # The latest method replaces the previous one

# Creating an object of the MathOperations class
math_op = MathOperations()
# print(math_op.add(1, 2))  # This would raise a TypeError because the first method is replaced
print(math_op.add(1, 2, 3))  # Calls the latest method



# 2. Run-Time Polymorphism (Dynamic Polymorphism)
# Run-time polymorphism is achieved through method overriding and is commonly used in inheritance. This allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
# Example (Method Overriding):

# Parent class
class Animal:
    def sound(self):
        return "Some sound"

# Child class
class Dog(Animal):
    def sound(self):  # Overriding the sound method
        return "Woof!"

# Another child class
class Cat(Animal):
    def sound(self):  # Overriding the sound method
        return "Meow!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.sound())  # Calls the appropriate method based on the object type

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
