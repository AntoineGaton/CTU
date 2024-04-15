print('Opening file myfile.txt.')
f = open('myfile.txt')  # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string
f.seek(0) # reset file pointer position
contents_lines = f.readlines() # read lines

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:\n', contents)
print('\nSecond line of myfile.txt:\n', contents_lines[1])