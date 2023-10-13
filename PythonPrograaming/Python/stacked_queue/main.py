from Stack import Stack
from Queue import Queue

# Stack operations
num_stack = Stack()
num_stack.push(45)
num_stack.push(56)
num_stack.push(11)

# Output stack
print('Stack after push:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

num_stack.pop()  # Pop 11

# Output final stack
print('Stack after pop:', end=' ')
node = num_stack.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print('\n')


# Queue operations
num_queue = Queue()
num_queue.push(17)
num_queue.push(24)
num_queue.push(18)

# Output queue
print('Queue after push:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

num_queue.pop()  # Pop 17

# Output final queue
print('Queue after pop:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

'''
A linked list is a linear collection of nodes, each holding data and a reference to the next node. 
It's versatile for insertions and deletions at any position but requires traversal for access. 
Queues, in contrast, adhere to the FIFO principle, where elements are added at the rear and removed from the front. 
They are used for ordered processing and can be implemented with various structures, including linked lists.
'''