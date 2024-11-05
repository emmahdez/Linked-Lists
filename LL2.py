"""
A method to print the linked list one element per line

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

    def print_list(self): #method to print list 
        temp = self.head # temp pointer set to the head of the list, used to traverse through the linked list (as opposed to an index in a normal list, linked list nodes are scattered in memory)
        while temp is not None: #while loop to traverse through list as long as the length of itself i.e as long as a pointer points to a node (not None)
            print(temp.value) #print current node value to which temp is pointing at 
            temp = temp.next # moves pointer to the next node in the list
        
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()
