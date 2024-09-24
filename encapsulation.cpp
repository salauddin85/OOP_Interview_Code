// # 1. Encapsulation
// # Encapsulation is the concept of bundling the data (attributes) and 
// # the methods (functions) that operate on that data into a single unit
// #  called an object. It helps to keep the data safe from outside 
// # interference and misuse.

#include <iostream>
using namespace std;

class Car {
private:
    string make;
    string model;
    int year;  // Private attribute (encapsulated)

public:
    Car(string mk, string mdl, int yr) {
        make = mk;
        model = mdl;
        year = yr;
    }

    void displayInfo() {
        cout << make << " " << model << ", " << year << endl;
    }
    
    void setYear(int yr) {
        year = yr;  // Setting the year using a method (encapsulation)
    }
};

int main() {
    Car car1("Toyota", "Corolla", 2020);
    car1.displayInfo();
    car1.setYear(2021);
    car1.displayInfo();
    return 0;
}
