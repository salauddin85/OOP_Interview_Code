#include <iostream>
using namespace std;

class MathOperations {
public:
    int add(int a, int b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
};

int main() {
    MathOperations mathOp;
    cout << mathOp.add(10, 20) << endl;  // 2 arguments
    cout << mathOp.add(10, 20, 30) << endl;  // 3 arguments
    return 0;
}
