def selection_sort(numbers):
   # Get the length of the list
   n = len(numbers)

   # Outer loop for iterating through the list
   for i in range(n - 1):
      # Find the index of the maximum element in the unsorted part
      max_index = i
      for j in range(i + 1, n):
         if numbers[j] > numbers[max_index]:
               max_index = j

      # Swap the found maximum element with the first element
      numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

      # Output the list after each iteration of the outer loop
      print(numbers)

# Input: Read a list of integers from the user
numbers = list(map(int, input().split()))

# Call the selection_sort function with the input list
selection_sort(numbers)
