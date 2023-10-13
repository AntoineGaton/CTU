# This function, backwards_alphabet(), takes a starting letter as input and recursively prints the alphabet letters in reverse order, starting from the given letter and ending at 'a'.

def backwards_alphabet(curr_letter):
    # Base case: If the current letter is 'a', print it.
    if curr_letter == 'a':
        print(curr_letter)
    else:
        # Recursive case: If the current letter is not 'a', print it and then calculate the previous letter using the ASCII value manipulation.
        print(curr_letter)
        # Look at footnote for comment...
        prev_letter = chr(ord(curr_letter) - 1)
        # Call the function recursively with the previous letter to continue printing the alphabet in reverse.
        backwards_alphabet(prev_letter)

# Ask the user to provide a starting letter for the backwards alphabet printing.
starting_letter = input("Give me a starting letter: ")

# Call the function with the user-provided starting letter to start the backwards alphabet printing.
backwards_alphabet(starting_letter)

"""
# This line of code calculates the previous letter in the English alphabet based on the current letter provided as input.
# It uses the built-in Python functions chr() and ord() to perform the conversion.

# The ord() function takes a single character as input and returns its Unicode code point (an integer representing the Unicode value of the character).
# For example, ord('a') returns 97, ord('b') returns 98, and so on.

# The chr() function takes an integer (Unicode code point) as input and returns the corresponding character.
# For example, chr(97) returns 'a', chr(98) returns 'b', and so on.

# In this line of code, the current letter (curr_letter) is converted to its Unicode code point using ord(curr_letter),
# then the integer value is decremented by 1 to get the code point of the previous letter in the alphabet.

# The resulting code point of the previous letter is then converted back to its character representation using chr(),
# and the result is stored in the variable prev_letter, which will hold the previous letter in the alphabet relative to the current letter.

"""