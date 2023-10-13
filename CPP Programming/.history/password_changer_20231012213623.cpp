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

   wait
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}