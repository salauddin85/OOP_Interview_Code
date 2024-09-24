# 2. Abstraction
# Abstraction means hiding the complex implementation
# details and showing only the essential information. 
# It allows us to focus on what an object does instead
# of how it does it.
# In Python, abstraction can be achieved using:

# Abstract Classes
# Interfaces


class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

payment = CreditCardPayment()
print(payment.pay(1000))



# 1. Abstract Classes
# An abstract class is a class that cannot be instantiated and usually contains one or more abstract methods that must be implemented by its subclasses. Abstract classes allow you to define methods that must be created within any child classes built from the abstract class.

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, no implementation

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method, no implementation

# Subclass inheriting from the abstract class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementation of abstract method

    def perimeter(self):
        return 2 * (self.width + self.height)  # Implementation of abstract method

# Subclass inheriting from the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Implementation of abstract method

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Implementation of abstract method

# Creating objects of the subclasses
rectangle = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle Area: {rectangle.area()}")      # Output: Rectangle Area: 15
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 16
print(f"Circle Area: {circle.area()}")            # Output: Circle Area: 50.24
print(f"Circle Perimeter: {circle.perimeter()}")  # Output: Circle Perimeter: 25.12




# 2. Interfaces
# In Python, there is no built-in support for interfaces like in some other programming languages. However, you can achieve similar functionality using abstract classes. An interface can be thought of as a class with only abstract methods (no implementation).

# Example (Using Abstract Classes as Interfaces):

from abc import ABC, abstractmethod

# Interface-like abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method

# Subclass implementing the interface
class Dog(Animal):
    def sound(self):
        return "Woof!"  # Implementation of abstract method

# Subclass implementing the interface
class Cat(Animal):
    def sound(self):
        return "Meow!"  # Implementation of abstract method

# Function demonstrating abstraction
def animal_sound(animal):
    print(animal.sound())  # Calls the appropriate method based on the object type

# Creating objects of the subclasses
dog = Dog()
cat = Cat()

# Demonstrating abstraction
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
