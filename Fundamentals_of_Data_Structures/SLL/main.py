from node import Node
from sll import SLL



# class Node:
#    def __init__(self, data):
#       # Constructor to initialize a new node with data and next as None
#       self.data = data
#       self.next = None

#    def print_linked_list(self):
#       # Method to print the linked list starting from the current node
#       current = self
#       while current:
#          print(str(current.data) + " -> ", end="")
#          current = current.next
#       print("None")

# # Display header for the linked list app
# print("=====================================")
# print("Singly Linked List App")
# print("=====================================")

# # Initialize the head of the linked list
# user_input = input("Enter your input to make the head: ")
# head = Node(user_input)
# current_node = head  # Keep track of the current node

# while True:
#    # Get user input to add a node to the end (type 'q' to quit)
#    user_input = input("Enter your input to add to the end (type 'q' to quit): ")

#    if user_input == "q":
#       break
#    elif user_input.strip():  # Check if the input is not empty
#       # Create a new node with user input and add it to the end
#       new_node = Node(user_input)
#       current_node.next = new_node
#       current_node = new_node
#    else:
#       print("Input is empty, try again.")

# # Display header for printing the linked list
# print("=====================================")
# print("Printing the linked list")
# print("=====================================")

# if head:
#    # Print the linked list if it is not empty
#    head.print_linked_list()
# else:
#    # Print a message if the linked list is empty
#    print("Linked list is empty.")
