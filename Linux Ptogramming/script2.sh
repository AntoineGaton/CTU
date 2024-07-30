#!/bin/bash
# This script demonstrates functions in Bash

# Define integer variables
FirstSum=0  # Initialize FirstSum to 0
SecondSum=0  # Initialize SecondSum to 0
Product=0  # Initialize Product to 0

# Function to add two numbers
Sum() {
    local a=$1  # First argument
    local b=$2  # Second argument
    return $(($a + $b))  # Return the sum of the two arguments
}

# Function to multiply two numbers
Multiplication() {
    local a=$1  # First argument
    local b=$2  # Second argument
    return $(($a * $b))  # Return the product of the two arguments
}

# Call Sum function and store results
Sum 100 200  # Call Sum with arguments 100 and 200
FirstSum=$?  # Store the result in FirstSum

Sum 300 400  # Call Sum with arguments 300 and 400
SecondSum=$?  # Store the result in SecondSum

# Call Multiplication function and store result
Multiplication $FirstSum $SecondSum  # Call Multiplication with FirstSum and SecondSum
Product=$?  # Store the result in Product

echo "FirstSum: $FirstSum"  # Print FirstSum
echo "SecondSum: $SecondSum"  # Print SecondSum
echo "Product: $Product"  # Print Product

echo "Script execution completed."  # Indicate script completion
exit 0  # Exit the script successfully
