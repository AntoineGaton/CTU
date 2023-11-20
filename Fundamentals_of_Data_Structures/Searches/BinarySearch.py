def BinarySearch(numbers, numbersSize, key):
   mid = 0
   low = 0
   high = numbersSize - 1
   
   while (high >= low):
      mid = (high + low) / 2
      if (numbers[mid] < key):
         low = mid + 1
      elif (numbers[mid] > key):
         high = mid - 1
      else:
         return mid
   return -1 # not found

def main():
   numbers = { 2, 4, 7, 10, 11, 32, 45, 87 }
   NUMBERS_SIZE = 8
   i = 0
   key = 0
   keyIndex = 0
   
   print("NUMBERS: ")
   
   for i in range(NUMBERS_SIZE):
      print(numbers[i] + " ")
      
   print()
   
   print("Enter a value: ")
   key = int(input())
   
   keyIndex = BinarySearch(numbers, NUMBERS_SIZE, key)
   
   if (keyIndex == -1):
      print(key + " was not found.")
   else:
      print("Found " + key + " at index " + keyIndex + ".")

if __name__ == '__main__':
   main()