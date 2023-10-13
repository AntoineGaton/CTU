# TODO: Write recursive digit_count() function here.
def digit_count(n):
    # Base case: when the number is less than 10, it has only one digit
    if n < 10:
        return 1
    else:
        # Recursive case: increase digit count by 1 and divide n by 10
        return 1 + digit_count(n // 10)

if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)