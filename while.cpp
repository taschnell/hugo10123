#include <iostream>
using namespace std;

int x = 0;
int y;

int main() {
   while (x < 10000) {
       cout << x << '\n';
       x += 1;
   };
   return 0;
}