#include <iostream>
using namespace std;
#include <unistd.h>182379

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
   cout << "***********************" << endl;
   
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}