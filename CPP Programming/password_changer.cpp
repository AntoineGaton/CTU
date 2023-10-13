#include <iostream>
using namespace std;
#include <unistd.h>

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

   cout << "***********************" << endl;
   cout <<  "Converting Password..." << endl;
   cout << "***********************" << endl;
   
   sleep(2);
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}