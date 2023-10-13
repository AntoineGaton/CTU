#include <iostream>    // Include the input/output stream library
#include <vector>      // Include the vector library
#include <string>      // Include the string library
#include <unordered_map> // Include the unordered_map library
#include <ctime>       // Include the C Standard Library for date and time
#include <cmath>       // Include the math library

// Class definition
class Person {
public:
    // Constructor
    Person(std::string name, int age) : name(name), age(age) {}

    // Member function
    void introduce() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }

private:
    std::string name;
    int age;
};

int main() {
    // Get the current date and time
    std::time_t currentTime = std::time(0);
    std::tm* now = std::localtime(&currentTime);

    int year = now->tm_year + 1900;
    int month = now->tm_mon + 1;
    int day = now->tm_mday;
    int hour = now->tm_hour;
    int minute = now->tm_min;
    int second = now->tm_sec;

    // Ternary operator for a simple condition
    int x = 10;
    int y = 20;
    int maxNumber = (x > y) ? x : y;

    // Math operations
    double squareRoot = std::sqrt(25);
    double power = std::pow(2, 3);
    double absoluteValue = std::abs(-7);

    // Variable declaration and initialization
    int integerNumber = 42;
    double doubleNumber = 3.14159;
    std::string text = "Hello, World!";

    // Vector (dynamic array) declaration and initialization
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Class instantiation
    Person person("Alice", 30);

    // Dictionary (unordered_map) declaration and initialization
    std::unordered_map<std::string, int> ages;
    ages["Alice"] = 30;
    ages["Bob"] = 25;
    ages["Charlie"] = 35;

    // Output data
    std::cout << "Current Date and Time: " << year << "-" << month << "-" << day << " " << hour << ":" << minute << ":" << second << std::endl;
    std::cout << "The maximum of " << x << " and " << y << " is " << maxNumber << std::endl;
    std::cout << "Square Root of 25: " << squareRoot << std::endl;
    std::cout << "2^3: " << power << std::endl;
    std::cout << "Absolute Value of -7: " << absoluteValue << std::endl;

    std::cout << "Integer Number: " << integerNumber << std::endl;
    std::cout << "Double Number: " << doubleNumber << std::endl;
    std::cout << "Text: " << text << std::endl;

    std::cout << "Numbers in the vector: ";
    for (int number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;

    // Call a member function of the class
    person.introduce();

    std::cout << "Ages in the dictionary:" << std::endl;
    for (const auto& entry : ages) {
        std::cout << entry.first << ": " << entry.second << " years old" << std::endl;
    }

    // End of the main function
    return 0;
}
