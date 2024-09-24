# 3. Constructor Overloading
# Constructor Overloading allows a class to have more than one constructor, each with different parameters. This lets you create objects in multiple ways.\


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def show(self):
        if self.name and self.age:
            return f"Name: {self.name}, Age: {self.age}"
        elif self.name:
            return f"Name: {self.name}"
        else:
            return "No information available"

person1 = Person("John", 30)
person2 = Person("Alice")
print(person1.show())
print(person2.show())
