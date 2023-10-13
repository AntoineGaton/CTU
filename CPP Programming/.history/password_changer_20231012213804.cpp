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

   //how to make program wait for 1 second
   //
   
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}#include <unistd.h>

int main()
{
   // Pause the program for 1 second
   sleep(1);

   return 0;
}
