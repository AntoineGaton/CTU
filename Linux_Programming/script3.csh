#!/bin/csh
# Script to demonstrate application process control

# Declare an integer variable for user input
set userInput = 0

# Prompt user for input
echo "Please enter a number:"
set userInput = $<

# Check if the number is less than, equal to, or greater than 100
if ($userInput < 100) then
    echo "The number is less than 100."
else if ($userInput == 100) then
    echo "The number is equal to 100."
else
    echo "The number is greater than 100."
endif

# While loop to decrement the number to 0
while ($userInput > 0)
    echo "Current value: $userInput"
    @ userInput--
end

echo "The script has ended. Goodbye."
exit 0
