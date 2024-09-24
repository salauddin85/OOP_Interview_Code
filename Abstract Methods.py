# 5. Abstract Methods
# An abstract method is a method that is declared but contains no implementation. Classes containing abstract methods cannot be instantiated directly and are meant to be inherited.



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())
