#include <iostream>
#include <iterator>
#include <list>

using namespace std;

string x;
string y;
string z;
list list_test;

int main() {
    cout << "Please Input a Term:\n";
    cin >> x;
    cout << "Please Input a Term:\n";
    cin >> y;
    cout << "Please Input a Term:\n";
    cin >> z;
    list_test.append(x);
    list_test.append(y);
    list_test.append(z);
    cout << list_test;

}