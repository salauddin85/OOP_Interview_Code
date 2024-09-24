# 1. Method Overloading
# Method Overloading refers to defining multiple methods with the same name but different parameters within the same class. This allows a function to handle different types or numbers of arguments.

# In Python, method overloading is not directly supported like in some other languages (e.g., C++), but you can achieve similar behavior using default arguments or *args and **kwargs.


class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        return a + b

math_op = MathOperations()
print(math_op.add(10, 20))  # 2 arguments
print(math_op.add(10, 20, 30))  # 3 arguments
