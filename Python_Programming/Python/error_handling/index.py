def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid data types for division!")
    else:
        return result

# Test cases
num1 = 10
num2 = 2
print("Result:", divide(num1, num2))

num1 = "10"
num2 = 2
print("Result:", divide(num1, num2))

num1 = 10
num2 = 0
print("Result:", divide(num1, num2))
