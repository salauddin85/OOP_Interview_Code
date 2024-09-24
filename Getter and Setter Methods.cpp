#include <iostream>
using namespace std;

class Person {
private:
    string name;  // Private attribute

public:
    Person(string n) : name(n) {}

    string getName() {
        return name;
    }

    void setName(string n) {
        name = n;
    }
};

int main() {
    Person person("John");
    cout << person.getName() << endl;
    person.setName("Alice");
    cout << person.getName() << endl;
    return 0;
}
