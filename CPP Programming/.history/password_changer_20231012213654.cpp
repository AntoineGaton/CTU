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

   //how to make it wait for 1 second
   this_thread::sleep_for(std::chrono::seconds(1));
   wait(1);

   cout << "Valid password: " << passwdStr << endl;

   return 0;
}