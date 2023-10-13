#include <iostream>
#include <string>
using namespace std;

int main() {
   string userText;
   int usaIndex;

   cout << "Enter text: ";
   getline(cin, userText);

   // At least one occurrence exists
   while (userText.find("Antoine") != string::npos) {// string::npos is a constant representing largest possible size of a string
      // Get index of first instance
      usaIndex = userText.find("Antoine");// find() returns index of first instance of string, or string::npos if not found

      // U.S.A. is 6 long
      userText.replace(usaIndex, userText.length(), "Gaton");// replace() replaces part of string with another string

   }

   cout << "New text: " << userText<< endl;

   return 0;
}