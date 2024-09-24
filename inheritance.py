
# n object-oriented programming (OOP), inheritance is the mechanism by which one class (child or subclass) can inherit the attributes and methods of another class (parent or superclass). In Python, inheritance allows for the reuse of code and the creation of a hierarchical relationship between classes.

# There are several types of inheritance in Python, and they differ based on the relationships between the parent and child classes.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Barks"

class Cat(Animal):
    def sound(self):
        return "Meows"

dog = Dog("Buddy")
print(dog.name, ":", dog.sound())

cat = Cat("Whiskers")
print(cat.name, ":", cat.sound())

# ---------------------------------
# 1. Single Inheritance
# In single inheritance, a child class inherits from only one parent class. This is the most basic form of inheritance.

# Parent class
class Animal:
    def sound(self):
        return "Some sound"

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Creating an object of the child class
dog = Dog()
print(dog.sound())  # Inherited method
print(dog.bark())   # Child's own method


# In the above example, Dog class inherits the sound() method from the Animal class.
# ----------------------------------------------
# 2. Multiple Inheritance
# In multiple inheritance, a child class can inherit from more than one parent class. This can allow a class to inherit attributes and methods from multiple sources.

# Parent class 1
class Father:
    def skills(self):
        return "Driving"

# Parent class 2
class Mother:
    def skills(self):
        return "Cooking"

# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def show_skills(self):
        return f"{self.skills()}"

# Creating an object of the child class
child = Child()
print(child.skills())  # Inherited from Father (since Father is first in the order of inheritance)


# ------------------------------------------------------------------------------------

# 3. Multilevel Inheritance
# In multilevel inheritance, a class is derived from a class that is already derived from another class. Essentially, there is a chain of inheritance.

# Grandparent class
class Animal:
    def sound(self):
        return "Some sound"

# Parent class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Child class inheriting from Dog
class Puppy(Dog):
    def play(self):
        return "Playing"

# Creating an object of the child class
puppy = Puppy()
print(puppy.sound())  # Inherited from Animal
print(puppy.bark())   # Inherited from Dog
print(puppy.play())   # Own method


# In this case, Puppy inherits from Dog, which in turn inherits from Animal. Thus, Puppy has access to methods from both Dog and Animal.
# ----------------------------------------------------------
# 4. Hierarchical Inheritance
# In hierarchical inheritance, multiple child classes inherit from a single parent class.

# Parent class
class Animal:
    def sound(self):
        return "Some sound"

# Child class 1 inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Child class 2 inheriting from Animal
class Cat(Animal):
    def meow(self):
        return "Meow!"

# Creating objects of the child classes
dog = Dog()
cat = Cat()

print(dog.sound())  # Inherited from Animal
print(dog.bark())   # Dog's own method
print(cat.sound())  # Inherited from Animal
print(cat.meow())   # Cat's own method


# In this example, both Dog and Cat inherit from the Animal class, which demonstrates hierarchical inheritance.

# ----------------------------------------------------------

# 5. Hybrid Inheritance
# Hybrid inheritance is a combination of two or more types of inheritance. It may involve a mix of single, multiple, and multilevel inheritance. Python’s method resolution order (MRO) comes into play to resolve any ambiguity in this type of inheritance.

# Parent class 1
class Father:
    def driving_skills(self):
        return "Good at driving"

# Parent class 2
class Mother:
    def cooking_skills(self):
        return "Good at cooking"

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def child_skills(self):
        return "Good at sports"

# Grandchild class inheriting from Child (Multilevel + Multiple)
class Grandchild(Child):
    def grandchild_skills(self):
        return "Good at painting"

# Creating an object of the grandchild class
grandchild = Grandchild()
print(grandchild.driving_skills())   # Inherited from Father
print(grandchild.cooking_skills())   # Inherited from Mother
print(grandchild.child_skills())     # Inherited from Child
print(grandchild.grandchild_skills())# Own method


# In this example, the Grandchild class inherits from the Child class, which itself inherits from both Father and Mother. This creates a hybrid inheritance pattern involving both multilevel and multiple inheritance.