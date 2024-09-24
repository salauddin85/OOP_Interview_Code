#include <iostream>
using namespace std;

class Shape {
public:
    virtual double area() = 0;  // Abstract method (pure virtual)
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

class Square : public Shape {
private:
    double side;

public:
    Square(double s) : side(s) {}

    double area() override {
        return side * side;
    }
};

int main() {
    Shape* shapes[2];
    shapes[0] = new Circle(5);
    shapes[1] = new Square(4);

    for (int i = 0; i < 2; i++) {
        cout << shapes[i]->area() << endl;
    }

    return 0;
}
