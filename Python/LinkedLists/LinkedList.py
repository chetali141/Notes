"""
Implementing the Linked List.
Things implemented so far:
1. Insert element in the start
2. Insert element in the end
3. Insert element at the Kth position
4. Size of the linked list (2 approaches)
5. Find an element in the linked list
"""

import intro

class LinkedList():

    def __init__(self, head):
        self.head = head
    
    # print whole linked list
    def __repr__(self):
        node = self.head
        nodes = []
        while(node != None):
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    # adding a node in the start
    def addFront(self, node):
        node.next = self.head
        self.head = node

    # adding a node in the end
    def addEnd(self, node):
        if self.head == None:
            self.head = node
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = node
    
    # adding a node at K th position
    def insertatKPosn(self, node, k):
        if k == 1:
            self.addFront(node)
            return "Adding node in starting."
        if recSize(self.head) < k:
            self.addEnd(node)
            return "Length of linked list is small than provided position. Adding node in end."
        temp = self.head
        for i in range (k-2):
            temp = temp.next
        var = temp.next
        temp.next = node
        node.next = var

# finding a data value in the linked list
def find(head, val):
    temp = head
    while temp!=None:
        if temp.data == val:
            return True
        temp = temp.next
    return False

#iterative code to print size of linked list
def size(head):
    temp = head
    count = 0
    while temp!=None:
        count = count + 1
        temp = temp.next
    return count

#recursive approach to print size of linked list
def recSize(head):
    if head == None:
        return 0
    return recSize(head.next) + 1

head = intro.Node(1)

sec_node = intro.Node(2)
head.next = sec_node

third_node = intro.Node(3)
sec_node.next = third_node

llHead = LinkedList(head)
print(llHead)

print(size(head))
print(recSize(head))

llHead.addFront(intro.Node(4))
print(llHead)

llHead.addEnd(intro.Node(5))
print(llHead)

llHead.insertatKPosn(intro.Node(6), 3)
print(llHead)

llHead.insertatKPosn(intro.Node(7), 1)
llHead.insertatKPosn(intro.Node(8), 10)

print(llHead)