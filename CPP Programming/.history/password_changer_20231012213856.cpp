#include <iostream>
using namespace std;

int main()
{
   string passwdStr;
   unsigned int i;

   cout << "Enter password: ";
   cin >> passwdStr;

   for (char &c : passwdStr)
   {
      if (!std::isalpha(c))
      {
         c = 'z';
      }
   }

   cout <<  "Converting Password..." << endl;
   sleep(2);
   cout << "***********************"
   
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}