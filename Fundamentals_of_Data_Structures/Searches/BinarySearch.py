def binary_search(numbers, key):
   # Variables to hold the low, middle and high indices
   # of the area being searched. Starts with entire range.
   low = 0
   mid = len(numbers) // 2
   high = len(numbers) - 1

   # Loop until "low" passes "high"
   while (high >= low):
      # calculate the middle index
      mid = (high + low) // 2

      # Cut the range to either the left or right half,
      # unless numbers[mid] is the key
      if (numbers[mid] < key):
         low = mid + 1
   
      elif (numbers[mid] > key):
         high = mid - 1
   
      else:
         return mid   

   return -1 # not found

def main():
   # Main program to test the binary_search()function   
   numbers = [2, 4, 7, 10, 11, 32, 45, 87]
   print('NUMBERS:', numbers)
      
   key = int(input('Enter an integer value: '))
   key_index = binary_search(numbers, key)
      
   if (key_index == -1):
      print('%d was not found.' % key)
   else:
      print('Found %d at index %d.' % (key, key_index))
      return 0
      
if __name__ == '__main__':
   main()
   
'''
Binary Search with recursion
BinarySearch(numbers, low, high, key) {
   if (low > high)
      return -1

   mid = (low + high) / 2
   if (numbers[mid] < key) {
      return BinarySearch(numbers, mid + 1, high, key)
   }
   else if (numbers[mid] > key) {
      return BinarySearch(numbers, low, mid - 1, key)
   }
   return mid
}
'''