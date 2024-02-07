""" 
1. Write a program that first reads in the name of an input file,  
followed by two strings representing the lower and upper bounds of a search range. 
2. The file should be read using the file.readlines() method. 
3. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. 
Your program should output all strings from the list that are within that range (inclusive of the bounds).
"""
def main():
    # Step 1: Read input file name and bounds from the user
    input_file = input()
    lower_bound = input()
    upper_bound = input()

    # Step 2: Read the contents of the file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Step 3: Check and print strings within the range
    for line in lines:
        word = line.strip()  # Remove the newline character at the end of each line
        if lower_bound <= word <= upper_bound:
            print(word)

if __name__ == "__main__":
    main()
