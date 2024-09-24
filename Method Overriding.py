# 2. Method Overriding
# Method Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. This allows the subclass to customize the behavior of a method inherited from the parent class.


class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Barks"

dog = Dog()
print(dog.sound())  # Output will be "Barks"
