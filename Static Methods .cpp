// 4. Static Methods
// Static Methods are methods that belong to the class, not to the object of the class. They do not modify the state of the object and are often used for utility or helper functions.

#include <iostream>
using namespace std;

class Math {
public:
    static int multiply(int a, int b) {
        return a * b;
    }
};

int main() {
    cout << Math::multiply(10, 20) << endl;  // Can call without creating an instance
    return 0;
}
