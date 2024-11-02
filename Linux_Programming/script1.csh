#!/usr/bin/tcsh
# This script reads environment variables from a configuration file and sets them.

# Check if the environment.cfg file exists
if (! -e environment.cfg) then
    echo "Error: environment.cfg file does not exist."  # Display error message if file does not exist
    exit 1  # Exit the script with an error code
endif

# Read environment variables into an array
set env_vars = ()  # Initialize an empty array
foreach line (`cat environment.cfg`)  # Loop through each line of the configuration file
    set env_vars = ($env_vars $line)  # Add the line to the array
end

# Loop through the array and set environment variables
foreach var ($env_vars)
    switch ($var)  # Check the value of the current array element
        case "enVar1":
            setenv enVar1 "value1"  # Set environment variable enVar1
            breaksw
        case "enVar2":
            setenv enVar2 "value2"  # Set environment variable enVar2
            breaksw
        case "enVar3":
            setenv enVar3 "value3"  # Set environment variable enVar3
            breaksw
    endsw
end

# Output environment variables to screen and file
echo "Environment variables:" > outputFile.txt  # Initialize the output file
foreach var (enVar1 enVar2 enVar3)
    echo $var  # Print the variable name to the screen
    echo $var >> outputFile.txt  # Append the variable name to the output file
end

echo "Script execution completed."  # Indicate script completion
exit 0  # Exit the script successfully
