// 3. Inheritance
// Inheritance allows a class to acquire the properties and behaviors of another class. This promotes code reuse and enables the creation of hierarchical relationships between classes.

#include <iostream>
using namespace std;

class Animal {
protected:
    string name;

public:
    Animal(string nm) : name(nm) {}

    virtual void sound() = 0;  // Abstract method (pure virtual)
};

class Dog : public Animal {
public:
    Dog(string nm) : Animal(nm) {}

    void sound() override {
        cout << name << " Barks" << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string nm) : Animal(nm) {}

    void sound() override {
        cout << name << " Meows" << endl;
    }
};

int main() {
    Dog dog("Buddy");
    dog.sound();

    Cat cat("Whiskers");
    cat.sound();
    return 0;
}
