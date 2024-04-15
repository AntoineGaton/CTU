# Read file contents
print ('Reading in data...')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average...')
total = 0
arr = []
for ln in lines:
    arr.append(int(ln))
    total += int(ln)

# Compute result
avg = total/len(lines)
print(f'Inputed Value: {arr[0]}, {arr[1]}, {arr[2]}')
print('Average Value:', avg)