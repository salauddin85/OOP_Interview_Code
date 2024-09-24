#include <iostream>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    // Constructor 1
    Person(string n, int a) : name(n), age(a) {}

    // Constructor 2
    Person(string n) : name(n), age(0) {}

    void show() {
        if (age == 0)
            cout << "Name: " << name << endl;
        else
            cout << "Name: " << name << ", Age: " << age << endl;
    }
};

int main() {
    Person person1("John", 30);
    Person person2("Alice");
    person1.show();
    person2.show();
    return 0;
}
