// 5. Abstract Methods
// An abstract method is a method that is declared but contains no implementation. Classes containing abstract methods cannot be instantiated directly and are meant to be inherited.

#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() = 0;  // Pure virtual function
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}

    double area() override {
        return 3.14 * radius * radius;
    }
};

int main() {
    Circle circle(5);
    cout << circle.area() << endl;
    return 0;
}
