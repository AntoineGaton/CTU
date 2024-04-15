# TODO: Write recursive fibonacci() function
def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
if __name__ == "__main__":
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
    