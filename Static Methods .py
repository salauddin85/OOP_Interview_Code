# 4. Static Methods
# Static Methods are methods that belong to the class, not to the object of the class. They do not modify the state of the object and are often used for utility or helper functions.

class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.multiply(10, 20))  # Can call without creating an instance of Math
