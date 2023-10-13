#include <iostream>  // Input/Output Stream Library
using namespace std;  // Use the std namespace
#include <vector> // Vector Library
#include <string> // String Library
#include <unordered_map> // Unordered Map Library
#include <ctime> // Time Library
#include <cmath> // Math Library

// A class is a blueprint for creating objects
class Person { 
// Public member functions
public: 
   // Constructor
   Person(string name, int age) : name(name), age(age) {}

   // Member function
   void introduce() {
      cout << "Hello, my name is " << name << " and I am " << age << " years old." << endl;
   }

// Private member variables
private:
    string name;
    int age;
};

// The main function
int main() {
    time_t currentTime = time(0); // Get the current time
    tm* now = localtime(&currentTime); // Convert the current time to the local time

    int year = now->tm_year + 1900; 
    int month = now->tm_mon + 1; // Month is 0 - 11, add 1 to get a jan-dec 1-12 concept
    int day = now->tm_mday; //
    int hour = now->tm_hour;
    int minute = now->tm_min;
    int second = now->tm_sec;

    int x = 10;
    int y = 20;
    int maxNumber = (x > y) ? x : y;

    double squareRoot = sqrt(25);
    double power = pow(2, 3);
    double absoluteValue = abs(-7);

    int integerNumber = 42;
    double doubleNumber = 3.14159;
    string text = "Hello, World!";

    vector<int> numbers = {1, 2, 3, 4, 5};

    Person person("Alice", 30);

    unordered_map<string, int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;
    ages["Charlie"] = 35;

    cout << "Current Date and Time: " << year << "-" << month << "-" << day << " " << hour << ":" << minute << ":" << second << endl;
    cout << "The maximum of " << x << " and " << y << " is " << maxNumber << endl;
    cout << "Square Root of 25: " << squareRoot << endl;
    cout << "2^3: " << power << endl;
    cout << "Absolute Value of -7: " << absoluteValue << endl;

    cout << "Integer Number: " << integerNumber << endl;
    cout << "Double Number: " << doubleNumber << endl;
    cout << "Text: " << text << endl;

    cout << "Numbers in the vector: ";
    for (int number : numbers) {
        cout << number << " ";
    }
    cout << endl;

    person.introduce();

    cout << "Ages in the dictionary:" << endl;
    for (const auto& entry : ages) {
        cout << entry.first << ": " << entry.second << " years old" << endl;
    }

    return 0;
}
