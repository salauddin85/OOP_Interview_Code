# 1. Encapsulation
# Encapsulation is the concept of bundling the data (attributes) and 
# the methods (functions) that operate on that data into a single unit
#  called an object. It helps to keep the data safe from outside 
# interference and misuse.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year  # Private attribute (encapsulated)

    def display_info(self):
        return f"{self.make} {self.model}, {self.__year}"
    
    def set_year(self, year):
        self.__year = year  # Setting the year using a method (encapsulation)

car1 = Car("Toyota", "Corolla", 2020)
print(car1.display_info())
car1.set_year(2021)
print(car1.display_info())



# 1. Public Encapsulation
# In Python, all class attributes and methods are public by default, meaning they can be accessed directly from outside the class.

class Car:
    def __init__(self, model, price):
        self.model = model  # Public attribute
        self.price = price  # Public attribute

    def show_details(self):  # Public method
        return f"Car Model: {self.model}, Price: {self.price}"

# Accessing public members
my_car = Car("Toyota", 20000)
print(my_car.model)  # Accessible
print(my_car.price)  # Accessible
print(my_car.show_details())  # Accessible


# 2. Protected Encapsulation
# Protected members are accessible within the class and its subclasses but should not be accessed directly from outside the class.

class Car:
    def __init__(self, model, price):
        self._model = model  # Protected attribute
        self._price = price  # Protected attribute

    def _show_details(self):  # Protected method
        return f"Car Model: {self._model}, Price: {self._price}"

class ElectricCar(Car):
    def battery_info(self):
        return f"{self._model} has a long battery life."

# Accessing protected members
my_electric_car = ElectricCar("Tesla", 50000)
print(my_electric_car._model)  # Accessible but not recommended
print(my_electric_car.battery_info())  # Protected attribute used in a subclass method



Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data within a single unit, such as a class. It also provides mechanisms to restrict access to certain details of an object, often referred to as data hiding.

In Python, encapsulation is typically implemented using access specifiers. These control how the attributes and methods of a class can be accessed. There are three main types of access specifiers used for encapsulation in Python:

1. Public
Attributes and methods that are publicly accessible.
They can be accessed directly from outside the class.
2. Protected
Attributes and methods that are intended to be accessed only from within the class or its subclasses.
In Python, a single underscore (_) before the attribute or method name is used to indicate that it is protected.
3. Private
Attributes and methods that are restricted from being accessed outside the class.
In Python, two underscores (__) before the attribute or method name are used to indicate that it is private.
1. Public Encapsulation
In Python, all class attributes and methods are public by default, meaning they can be accessed directly from outside the class.

Example (Public Encapsulation):
python
Copy code
class Car:
    def __init__(self, model, price):
        self.model = model  # Public attribute
        self.price = price  # Public attribute

    def show_details(self):  # Public method
        return f"Car Model: {self.model}, Price: {self.price}"

# Accessing public members
my_car = Car("Toyota", 20000)
print(my_car.model)  # Accessible
print(my_car.price)  # Accessible
print(my_car.show_details())  # Accessible
# -----------------------------------------------
# 2. Protected Encapsulation
# Protected members are accessible within the class and its subclasses but should not be accessed directly from outside the class.


class Car:
    def __init__(self, model, price):
        self._model = model  # Protected attribute
        self._price = price  # Protected attribute

    def _show_details(self):  # Protected method
        return f"Car Model: {self._model}, Price: {self._price}"

class ElectricCar(Car):
    def battery_info(self):
        return f"{self._model} has a long battery life."

# Accessing protected members
my_electric_car = ElectricCar("Tesla", 50000)
print(my_electric_car._model)  # Accessible but not recommended
print(my_electric_car.battery_info())  # Protected attribute used in a subclass method
# In the above example:

# _model and _price are protected attributes, so they can be accessed but it’s a convention not to access them directly.
# _show_details() is a protected method, and can be used within the class or its subclasses.

# ------------------------------
# 3. Private Encapsulation
# Private members are accessible only within the class itself and cannot be accessed directly from outside the class. This is achieved by using a double underscore (__) before the attribute or method name.

class Car:
    def __init__(self, model, price):
        self.__model = model  # Private attribute
        self.__price = price  # Private attribute

    def __show_details(self):  # Private method
        return f"Car Model: {self.__model}, Price: {self.__price}"

    def get_details(self):
        # Accessing private attributes within the class
        return self.__show_details()

# Accessing private members
my_car = Car("BMW", 40000)
# print(my_car.__model)  # Error: Cannot access private attribute directly
# print(my_car.__show_details())  # Error: Cannot access private method directly
print(my_car.get_details())  # Accessing private method through a public method
