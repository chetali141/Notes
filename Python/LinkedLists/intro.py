#Defining a Node class
class Node:

    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    #used to print data stored in the object
    def __repr__(self):
        return str(self.data)


 # adding head node   
head = Node(1)

# adding second node and maintaining the next node's place
sec_node = Node(2)
head.next = sec_node

third_node = Node(3)
sec_node.next = third_node

# print(head)
# print(sec_node)
# print(third_node)

# finding an element in the linked list
def find(head, val):
    temp = head
    while temp!=None:
        if temp.data == val:
            return True
        temp = temp.next
    return False


# print(find(head, 5))
# print(find(head, 3))
