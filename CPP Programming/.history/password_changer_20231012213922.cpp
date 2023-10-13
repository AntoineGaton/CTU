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
   cout << "***********************" << endl;
   
   cout << "Valid password: " << passwdStr << endl;

   return 0;
}#include <iostream>
#include <chrono>
#include <thread>

int main() {
   std::cout << "Delaying program for 3 seconds..." << std::endl;
   std::this_thread::sleep_for(std::chrono::seconds(3));
   std::cout << "Program resumed." << std::endl;
   return 0;
}
