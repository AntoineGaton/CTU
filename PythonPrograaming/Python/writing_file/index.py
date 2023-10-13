num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open('myfile.txt', 'w+')
f.write(str(num1))
f.write(' + ')
f.write(str(num2))
f.write(' = ')
f.write(str(num3))
f.seek(0)
print(f.read())
f.close()