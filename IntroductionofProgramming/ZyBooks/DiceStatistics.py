#zyDE 3.7.1: Dice statistics
import random

def roll_dice():
    return random.randint(1, 6)

def calculate_sum(num_rolls):
    sums = [0] * 11
    for _ in range(num_rolls):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        sums[total-2] += 1
    return sums

def print_histogram(sums):
    for i, count in enumerate(sums):
        print(f'{i+2}: {"*" * count}')

num_sixes = 0
num_sevens = 0

while True:
    # Get user input
    user_input = input("Enter the number of times to roll the dice (enter 'q' to quit): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'q':
        break

    # Convert user input to integer
    num_rolls = int(user_input)
    
    # Check if input is valid
    if num_rolls < 1:
        print("Invalid input. Please enter a positive number or 'q' to quit.")
        continue

    # Calculate sums of dice rolls
    sums = calculate_sum(num_rolls)
    
    # Print histogram
    print_histogram(sums)

    # Update totals for sixes and sevens
    num_sixes += sums[4]  # Count of 6s (index 4 in sums list)
    num_sevens += sums[5]  # Count of 7s (index 5 in sums list)

# Print final totals
print(f"Total sixes rolled: {num_sixes}")
print(f"Total sevens rolled: {num_sevens}")