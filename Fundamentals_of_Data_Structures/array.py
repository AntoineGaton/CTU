#app dealing with arrays

print("=====================================")
print("Array App")
print("=====================================")
print("1: Create an fixed length array.")
print("2: Create an dynamic array.")
print("=====================================")

choice = int(input("Enter your choice: "))

match choice:
   case 1:
      print("=====================================")
      print("Fixed Length Array")
      print("=====================================")
      # Initialize the array
      length = int(input("Enter the length of the array: "))
      array = [None] * length
      print("=====================================")
      while array