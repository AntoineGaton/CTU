from Node import Node
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item
