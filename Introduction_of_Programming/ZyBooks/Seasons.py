# Get user input
input_month = input("Enter a month: ")
print('Enter a day: ', end='')
input_day = int(input())

# Define the valid months
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# Check if the input month is valid
if input_month not in months:
    print('Invalid')

# Check specific conditions for each month
elif input_month == 'January':
    if not (1 <= input_day <= 31):
        print('Date Invalid')
    else:
        print('Season: Winter')

elif input_month == 'February':
    if not (1 <= input_day <= 28):
        print('Date Invalid')
    else:
        print('Season: Winter')

elif input_month == 'March':
    if 1 <= input_day < 20:
        print('Season: Winter')
    elif 20 <= input_day <= 31:
        print('Season: Spring')
    else:
        print('Date Invalid')

elif input_month == 'April':
    if not (1 <= input_day <= 30):
        print('Date Invalid')
    else:
        print('Season: Spring')

elif input_month == 'May':
    if not (1 <= input_day <= 31):
        print('Date Invalid')
    else:
        print('Season: Spring')

elif input_month == 'June':
    if 1 <= input_day <= 20:
        print('Season: Spring')
    elif 21 <= input_day <= 30:
        print('Season: Summer')
    else:
        print('Date Invalid')

elif input_month == 'July' or input_month == 'August':
    if not (1 <= input_day <= 31):
        print('Date Invalid')
    else:
        print('Season: Summer')

elif input_month == 'September':
    if not (1 <= input_day <= 30):
        print("Date Invalid")
    elif 1 <= input_day <= 21:
        print("Season: Summer")
    else:
        print("Season: Autumn")

elif input_month == 'October':
    if not (1 <= input_day <= 31):
        print('Date Invalid')
    else:
        print('Season: Autumn')

elif input_month == 'November':
    if not (1 <= input_day <= 30):
        print('Date Invalid')
    else:
        print('Season: Autumn')

elif input_month == 'December':
    if 1 <= input_day <= 20:
        print('Season: Autumn')
    elif 21 <= input_day <= 31:
        print('Season: Winter')
    else:
        print('Date Invalid')