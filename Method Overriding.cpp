// Method Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. This allows the subclass to customize the behavior of a method inherited from the parent class.

#include <iostream>
using namespace std;

class Animal {
public:
    virtual void sound() {
        cout << "Some sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Barks" << endl;
    }
};

int main() {
    Dog dog;
    dog.sound();  // Output will be "Barks"
    return 0;
}
