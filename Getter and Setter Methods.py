# Getter and Setter methods allow access and modification of private class variables.
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("John")
print(person.get_name())
person.set_name("Alice")
print(person.get_name())
