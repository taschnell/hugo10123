#include <iostream>
#include <iterator>
#include <array>
using namespace std;

string x;
string y;
string z;
int i;
string arraytest[3];

int main() {
    cout << "Please Input a Term:\n";
    cin >> x;
    cout << "Please Input a Term:\n";
    cin >> y;
    cout << "Please Input a Term:\n";
    cin >> z;
    cout << "\n\n";
    arraytest[0] = x;
    arraytest[1] = y;
    arraytest[2] = z;
    for (arraytest[i]; i++; cout << i){}
    
    cout << arraytest;

    int i = 0;
    for (cout << "\n\nstart\n"; i < 10;) {
        cout << i;
        i += 1;
    }
}