// 2. Abstraction
// Abstraction means hiding the complex implementation details and showing only the essential information. It allows us to focus on what an object does instead of how it does it.


#include <iostream>
using namespace std;

class Payment {
public:
    virtual void pay(int amount) = 0;  // Abstract method (pure virtual)
};

class CreditCardPayment : public Payment {
public:
    void pay(int amount) override {
        cout << "Paid " << amount << " using Credit Card" << endl;
    }
};

class PayPalPayment : public Payment {
public:
    void pay(int amount) override {
        cout << "Paid " << amount << " using PayPal" << endl;
    }
};

int main() {
    Payment* payment = new CreditCardPayment();
    payment->pay(1000);
    return 0;
}
