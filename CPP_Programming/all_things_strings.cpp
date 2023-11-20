#include <iostream>
#include <string>
using namespace std;

// Function to concatenate two strings
string concatenateStrings(string firstName, string lastName)
{
   return firstName + " " + lastName;
}

// Function to get the length of a string
int getStringLength(string text)
{
   return text.length();
}

// Function to extract a substring from a string
string getSubstring(string text, int start, int length)
{
   return text.substr(start, length);
}

// Function to check if a string contains a specific substring
bool containsSubstring(string sentence, string word)
{
   return sentence.find(word) != string::npos;
}

// Function to read a string from the user
string getInputString()
{
   string userInput;
   cout << "Enter a string: ";
   cin >> userInput;
   return userInput;
}

// Function to replace all occurrences of a substring in a string
string replaceSubstring(string text, string oldStr, string newStr)
{
   size_t foundPos;
   while ((foundPos = text.find(oldStr)) != string::npos)
   {
      text.replace(foundPos, oldStr.length(), newStr);
   }
   return text;
}

int main()
{
   // Concatenate strings
   string fullName = concatenateStrings("John", "Doe");
   cout << "Concatenated Name: " << fullName << endl;

   // Get string length
   int length = getStringLength("Hello, World!");
   cout << "String Length: " << length << endl;

   // Extract a substring
   string subText = getSubstring("This is a sample text", 5, 7);
   cout << "Substring: " << subText << endl;

   // Check if a string contains a specific substring
   bool containsWord = containsSubstring("The quick brown fox", "brown");
   cout << "Contains 'brown': " << (containsWord ? "Yes" : "No") << endl;

   // Read a string from the user
   string userInput = getInputString();
   cout << "User Input: " << userInput << endl;

   // Replace substrings
   string replacedText = replaceSubstring("I love apples. Apples are great!", "apples", "bananas");
   cout << "Replaced Text: " << replacedText << endl;

   return 0;
}
