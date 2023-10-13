def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1   # not found


numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', end=' ')
for num in numbers:
    print(str(num), end=' ')
print()

key = int(input('Enter a value: '))
key_index = linear_search(numbers, key)

if key_index == -1:
    print(str(key) + ' was not found.')
else:
    print('Found ' + str(key) + ' at index ' + str(key_index) + '.')