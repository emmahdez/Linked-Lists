"""
A method to append a new node to the end of a list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value) #call to Node class
        if self.head is None: # if the head of the list points to None (checking the list is empty)
            self.head = new_node # point head to new node
            self.tail = new_node # point tail to the same new node
        else:
            self.tail.next = new_node # have tail of the list point to the new node
            self.tail = new_node # the tail is now the new node
            
        self.length += 1 #increase the length of the list




my_linked_list = LinkedList(1)
my_linked_list.make_empty() #empty list first 

my_linked_list.append(1) #appending the value 1 to the list 
my_linked_list.append(2) #appending the value 2 to the end of the list 

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list() #final linked list 