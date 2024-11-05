"""
Constructing singly linked list

"""

class Node:  # node class to represent an individual node
    def __init__(self,value):
        self.value = value
        self.next = None 
        
class LinkedList: # linkedlist class to manage the linked list
    def __init__(self, value):
        new_node = Node(value) #creating a new node using the Node class
        self.head = new_node # the head of the list is set to the new node
        self.tail = new_node 
        self.length = 1 # the length of the list



my_linked_list = LinkedList(4) 

print('Head:', my_linked_list.head.value) 
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)