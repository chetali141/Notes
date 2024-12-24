"""
Given 2 head pointers of a linked list.
1. Find if both the linkedlist intersect or not.
"""

import node
import LinkedList as LL

# unoptimized solution
# def yLinkedList(head1, head2):
#     while head1.next is not None:
#         temp = head2
#         while temp.next is not None:
#             if head1.next == temp.next:
#                 return True
#             temp = temp.next
#         head1 = head1.next
#     return False


# optimized using hashing
# def yLinkedList(head1, head2):
#     dict = {}
#     while head1 is not None:
#         dict[head1.next] = head1.data
#         head1 = head1.next
#     print("dictionary:" + str(dict))
#     while head2.next is not None:
#         if head2.next in dict:
#             return True
#         head2 = head2.next
#     return False

# optimized solution
def yLinkedList(head1, head2):
    size1 = LL.recSize(head1)
    size2 = LL.recSize(head2)
    
    if size1 > size2:
        diff = size1 - size2
        for i in range(diff):
            head1 = head1.next
    else:
        diff = size2 - size1
        for i in range(diff):
            head2 = head2.next
    while(head1 is not None and head2 is not None):
        if head1 == head2:
          return True
        head1 = head1.next
        head2 = head2.next
    return False

# Creating Linked List 1
head1 = node.Node(1)
sNode1 = node.Node(2)
head1.next = sNode1
tNode1 = node.Node(3)
sNode1.next = tNode1
fNode1 = node.Node(4)
tNode1.next = fNode1
llHead1 = LL.LinkedList(head1)
print("First Linked List: "+str(llHead1))


# Creating Linked list 2
head2 = node.Node(5)
sNode2 = node.Node(6)
head2.next = sNode2
sNode2.next = tNode1 #pointing to same element from this Node onwards
llHead2 = LL.LinkedList(head2)
print("Second Linked List: "+str(llHead2))

# Creating Linked list 3
head3 = node.Node(10)
head3.next = tNode1 #pointing to same element from this Node onwards
llHead3 = LL.LinkedList(head3)
print("Third Linked List: "+str(llHead3))

# Creating Linked list 4
head4 = node.Node(10)
sNode4 = node.Node(11)
tNode4 = node.Node(12)
head4.next = sNode4
sNode4.next = tNode4
llHead4 = LL.LinkedList(head4)
print("Fourth Linked List: "+str(llHead4))

# Creating Linked list 3
head5 = node.Node(10)
sNode5 = node.Node(11)
tNode5 = node.Node(12)
fNode5 = node.Node(13)
head5.next = sNode5
sNode5.next = tNode5
tNode5.next = fNode5
fNode5.next = tNode1 #pointing to same element from this Node onwards
llHead5 = LL.LinkedList(head5)
print("Fourth Linked List: "+str(llHead5))

print(yLinkedList(head1, head2)) # same number of elements before intersection
print(yLinkedList(head1, head3)) # different number of elements before intersection
print(yLinkedList(head1, head4)) # no intersection
print(yLinkedList(head1, head5))
