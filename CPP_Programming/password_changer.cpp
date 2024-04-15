#include <iostream>
using namespace std;
#include <unistd.h>

int main()
{
   changeNumberToLetter();
   cout << "***********************" << endl;
   changeNumberToNumber();
   cout << "***********************" << endl;
   goodPassword();
   
   return 0;
}

void changeNumberToLetter()
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

}

void changeNumberToNumber(){
   string passwordStr;
   int i;
   
   cin >> passwordStr;
   i = 0;

   string searchString = "1111";
   string replacementStr = "2785";
   size_t foundPos;

   while ((foundPos = passwordStr.find(searchString)) != string::npos) {
      passwordStr.replace(foundPos, searchString.length(), replacementStr);
   }

   cout << "Updated password: " << passwordStr << endl;
}

void goodPassword(){
    string keyString;
   bool goodPassword = true;
   int digitCount = 0;
   
   cin >> keyString;
   
   for (char c : keyString) {
      if (isdigit(c)) {
         digitCount++;
      }
   }

   if (digitCount >= 6 || keyString.length() > 9) {
      goodPassword = false;
   }
    
   if (goodPassword) {
      cout << "Valid" << endl;
   }
   else {
      cout << "Invalid" << endl;
   }
}