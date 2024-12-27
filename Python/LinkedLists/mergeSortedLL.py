"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
"""

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

def mergeSortedLL(list1,list2):
    dummy = node = ListNode()
    while list1 and list2:
        if list1.val > list2.val:
            node.next = list2
            list2 = list2.next
        else:
            node.next = list1
            list1 = list1.next
        node = node.next
    
    node.next = list1 or list2
    return dummy.next

head = ListNode(1)
sec_node = ListNode(3)
head.next = sec_node
third_node = ListNode(5)
sec_node.next = third_node

head1 = ListNode(2)
sec_node1 = ListNode(4)
head1.next = sec_node1
third_node1 = ListNode(6)
sec_node1.next = third_node1

mergedList = mergeSortedLL(head, head1)

print(printLinkedList(mergedList))
