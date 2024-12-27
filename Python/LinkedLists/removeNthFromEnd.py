"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    node = head
    nodes = []
    while(node != None):
        nodes.append(str(node.val))
        node = node.next
    nodes.append("None")
    return " -> ".join(nodes)

def removeNthFromEnd(head, n: int):
    size = 0
    temp = head

    while temp is not None:
        size += 1
        temp = temp.next
    print(size)

    if n == 1 and size == 1:
        head = None
    elif size - n == 0:
        return head.next
    else:    
        # n from end means size-n from starting
        temp = head
        for i in range (size - n - 1):
            temp = temp.next
        print(temp)
        var = temp.next
        print(var)
        temp.next = var.next
    
    return head

head = ListNode(1)
node2 = ListNode(2)
head.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

ll = removeNthFromEnd(head, 2)
print(printLinkedList(ll))
