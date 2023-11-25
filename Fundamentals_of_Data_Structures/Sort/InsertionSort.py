def InsertionSort(numbers, numbersSize):
   i = 1
   j = 0
   temp = 0  # Temporary variable for swap
   
   while i < numbersSize: 
      j = i
      # Insert numbers[i] into sorted part
      # stopping once numbers[i] in correct position
      while j > 0 and numbers[j] < numbers[j - 1]:      
         # Swap numbers[j] and numbers[j - 1]
         temp = numbers[j]
         numbers[j] = numbers[j - 1]
         numbers[j - 1] = temp
         j -= 1
      i += 1
   return numbers

def main():
   numbers = [10, 2, 78, 4, 45, 32, 7, 11 ]
   
   print("UNSORTED: ")
   for i in numbers:
      print(str(i), end=" ")
      
   print()
   
   numbers = InsertionSort(numbers, len(numbers))
   
   print("SORTED: ")
   for i in numbers:
      print(str(i), end=" ")
      
   print()

if __name__ == '__main__':
   main()  