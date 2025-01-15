"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head) -> bool:
    lldict = {}
    while head is not None:
        if head in lldict:
            return True
        else:
            lldict[head] = 1
        head = head.next
    return False


head = Node(1)
sNode = Node(2)
tNode = Node(3)
fNode = Node(4)
head.next = sNode
sNode.next = tNode
tNode.next = fNode
fNode.next = sNode

print(hasCycle(head))

head = Node(1)
sNode = Node(2)
tNode = Node(3)
fNode = Node(4)
head.next = sNode
sNode.next = tNode
tNode.next = fNode
fNode.next = None

print(hasCycle(head))
