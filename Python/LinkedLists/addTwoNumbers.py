"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
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

def addTwoNumbers(l1, l2):

    l3 = node.Node(0)
    curr = l3

    carry = 0
    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        sum = val1 + val2 + carry
        carry = sum//10
        sum = sum%10
            
        curr.next = node.Node(sum)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return l3.next

head1 = node.Node(2)
head1.next= node.Node(4)
head1.next.next = node.Node(3)

head2 = node.Node(5)
head2.next = node.Node(6)
head2.next.next = node.Node(4)

sol = addTwoNumbers(head1, head2)

print(printLinkedList(sol))
