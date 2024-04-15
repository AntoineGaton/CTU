Merge(numbers, i, j, k) {
   mergedSize = k - i + 1                // Size of merged partition
   mergePos = 0                          // Position to insert merged number
   leftPos = 0                           // Position of elements in left partition
   rightPos = 0                          // Position of elements in right partition
   mergedNumbers = new int[mergedSize]   // Dynamically allocates temporary array
                                         // for merged numbers
   
   leftPos = i                           // Initialize left partition position
   rightPos = j + 1                      // Initialize right partition position
   
   // Add smallest element from left or right partition to merged numbers
   while (leftPos <= j && rightPos <= k) {
      if (numbers[leftPos] <= numbers[rightPos]) {
         mergedNumbers[mergePos] = numbers[leftPos]
         ++leftPos
      }
      else {
         mergedNumbers[mergePos] = numbers[rightPos]
         ++rightPos
         
      }
      ++mergePos
   }
   
   // If left partition is not empty, add remaining elements to merged numbers
   while (leftPos <= j) {
      mergedNumbers[mergePos] = numbers[leftPos]
      ++leftPos
      ++mergePos
   }
   
   // If right partition is not empty, add remaining elements to merged numbers
   while (rightPos <= k) {
      mergedNumbers[mergePos] = numbers[rightPos]
      ++rightPos
      ++mergePos
   }
   
   // Copy merge number back to numbers
   for (mergePos = 0; mergePos < mergedSize; ++mergePos) {
      numbers[i + mergePos] = mergedNumbers[mergePos]
   }
}

MergeSort(numbers, i, k) {
   j = 0
   
   if (i < k) {
      j = (i + k) / 2  // Find the midpoint in the partition
      
      // Recursively sort left and right partitions
      MergeSort(numbers, i, j)
      MergeSort(numbers, j + 1, k)
      
      // Merge left and right partition in sorted order
      Merge(numbers, i, j, k)
   }
}

main() {
   numbers = { 10, 2, 78, 4, 45, 32, 7, 11 }
   NUMBERS_SIZE = 8
   i = 0
   
   print("UNSORTED: ")
   for(i = 0; i < NUMBERS_SIZE; ++i) {
      print(numbers[i] + " ")
   }
   printLine()
   
   MergeSort(numbers, 0, NUMBERS_SIZE - 1)
   
   print("SORTED: ")
   for(i = 0; i < NUMBERS_SIZE; ++i) {
      print(numbers[i] + " ")
   }
   printLine()
}