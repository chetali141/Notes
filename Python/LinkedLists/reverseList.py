"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""

import node

def printLinkedList(head):
    node = head
    nodes = []
    while(node != None):
        nodes.append(str(node.data))
        node = node.next
    nodes.append("None")
    return " -> ".join(nodes)

def reverseList(head):
        prev, current = None, head

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
 

head = node.Node(1)
sec_node = node.Node(2)
head.next = sec_node
third_node = node.Node(3)
sec_node.next = third_node

print(printLinkedList(head))
prev = reverseList(head)
print(printLinkedList(prev))
