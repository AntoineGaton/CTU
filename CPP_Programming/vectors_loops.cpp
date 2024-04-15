
#include <iostream>
#include <vector>
using namespace std;

int main() {
   int sizeVector;

   cout << "Enter vector size: ";
   cin >> sizeVector;

   vector<int> userVals(sizeVector); // User values
   unsigned int i;                 // Loop index
   
   cout << "Enter " << sizeVector << " integer values..." << endl;
   for (i = 0; i < userVals.size(); ++i) {
      cout << "Value: ";
      cin >> userVals.at(i);
   }
   
   cout << "You entered: ";
   for (i = 0; i < userVals.size(); ++i) {
      cout << userVals.at(i) << " ";
   }
   cout << endl;
   
   return 0;
}