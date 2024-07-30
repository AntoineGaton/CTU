"""
Script for Key-Value Store Operations

Description:
This script demonstrates a basic implementation of a key-value store using a dictionary in Python.
The dictionary contains 50 state-capital pairs as key-value entries. It includes functions to
enumerate the contents of the key-value pairs, list all keys, list all values, and replace the
value of a specified key.

Author: Antoine Gaton
Email: antoine.gaton@student.ctuonline.edu
Date: June 30, 2024

Dependencies:
- None (built-in Python libraries are used)

Usage:
1. Ensure you have Python installed on your system.
2. Run the script:
   python key_value_store.py

Dictionary Data:
- The dictionary contains 50 state-capital pairs for demonstration purposes.
"""

# Creating a dictionary with 50 state-capital pairs
states_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Function to enumerate the contents of key-value pairs
def enumerate_contents(dictionary):
    """
    Prints the key-value pairs in the dictionary.

    Parameters:
    dictionary (dict): The dictionary to enumerate.
    """
    for key, value in dictionary.items():
        print(f'The capital of {key} is {value}')

# Function to list all keys in the dictionary
def list_keys(dictionary):
    """
    Lists all keys in the dictionary.

    Parameters:
    dictionary (dict): The dictionary whose keys are to be listed.

    Returns:
    list: A list of keys in the dictionary.
    """
    return list(dictionary.keys())

# Function to list all values in the dictionary
def list_values(dictionary):
    """
    Lists all values in the dictionary.

    Parameters:
    dictionary (dict): The dictionary whose values are to be listed.

    Returns:
    list: A list of values in the dictionary.
    """
    return list(dictionary.values())

# Function to replace the value of key number "1"
def replace_value(dictionary, key, new_value):
    """
    Replaces the value of the specified key with a new value.

    Parameters:
    dictionary (dict): The dictionary to update.
    key: The key whose value is to be replaced.
    new_value: The new value to assign to the key.
    """
    if key in dictionary:
        dictionary[key] = new_value
    else:
        print(f'Key {key} not found in the dictionary.')

# Main execution
if __name__ == "__main__":
    # Enumerate the contents of the dictionary
    print("Enumerating contents of the dictionary:")
    enumerate_contents(states_capitals)
    
    print("\n------------------------------------------\n")
    
    # List all keys
    print("List of all keys:")
    print(list_keys(states_capitals))
    
    print("\n------------------------------------------\n")
    
    # List all values
    print("List of all values:")
    print(list_values(states_capitals))

    print("\n------------------------------------------\n")

    # Replace value of key 'Alabama' with a new value 'New Montgomery'
    print("Replacing value of key 'Alabama' with 'New Montgomery':")
    replace_value(states_capitals, 'Alabama', 'New Montgomery')
    print("Updated dictionary:")
    enumerate_contents(states_capitals)
