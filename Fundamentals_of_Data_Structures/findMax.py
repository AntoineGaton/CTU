def findMax(arr):
   max = arr[0]
   
   for i in arr:
      if i > max:
         max = i
   
   return max

arr = []
print("Enter 10 numbers: ")   
for i in range(0, 10):
   num = int(input())
   arr.append(num)
   
   
   

max = findMax(arr)

print("Max is: " + str(max))

# Python	Python standard library	list, set, dict, deque