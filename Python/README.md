# Python - Notes

The repository contains my Python programming codes.

## Basic Questions

|File Name | Descripton |
|---|---|
| [Design Patterns](/Python/DesignPatterns.py) | The file contains code for some basic design patterns asked to print using loops. |
| [Password Generator](/Python/PasswordGenerator.py) | This file contains a program which can generate password for you or secure your password. |
| [Tower of Hanoi](/Python/TowerOfHanoi.py) | This file contains the solution to the Tower of Hanoi mathematical puzzle. |
| [Palindrome Number](/Python/PalindromeNumber.py) | This file contains the solution to the palindrome problem. |
| [Pascal's Triangle](/Python/PascalTriangle.py) |  |

## Arrays

|File Name | Descripton |
|---|---|
| [Reverse Array](/Python/Arrays/reverseArray.py) | Reverse the given array without using extra space. |
| [Rotate Array](/Python/Arrays/rotateArray.py) | Rotate a given array from left to right 'k' times. |
| [Sum of all elements between range](/Python/Arrays/sumBtwLandR.py) | Calculate sum of all the elements of the array present between the given left and right index. |
| [Equilibrium Index](/Python/Arrays/equilibriumIndex.py) | Find the equilibrium index 'i' such that the sum of all elements on it's left is equal to the sum of all the elements on it's right. |
| [Pick from both sides](/Python/Arrays/pickFromBothSides.py) | Pick 'k' elements from left or right or both the sides of the array to find the maximum sum. |
| [Sum of all odd or even elements between range](/Python/Arrays/sumRangeOddEven.py) | Calculate sum of all elements present on odd or even index between the given range from left to right. |
| [Leader Element](/Python/Arrays/leaders.py) | Find the leader element in the given array. A element is leader if it is strictly greater than all the elements to its right. |
| [Closest Min Max](/Python/Arrays/closestMinMax.py) | . |
| [Subarray](/Python/Arrays/subarray.py) | Print all the subarrays. |
| [Subarray of length k](/Python/Arrays/subarrayK.py) | . |
| [Maximum subarray sum](/Python/Arrays/maxSubarraySum.py) | . |
| [Maximum subarray sum of length k](/Python/Arrays/maxSubarraySumK.py) | . |
| [Sum of all subarray sum](/Python/Arrays/allSubarraySum.py) | . |
| [All diagonals of a square matrix](/Python/Arrays/diagonalSquare.py) | . |
| [Product Except Self](/Python/Arrays/productExceptSelf.py) | Given an array, find product of all elements in array except self. |

## Strings

|File Name | Description |
|---|---|
| [Count Pairs](/Python/Strings/countPairs.py) | . |
| [Sort Lowercase](/Python/Strings/sortLowercase.py) | . |
| [Reverse Substring](/Python/Strings/reverseSubstring.py) | . |
| [Valid Palindrome](/Python/Strings/validPalindrome.py) | . |
| [Valid Palidrome Substring](/Python/Strings/validPalindromeSubstring.py) | . |
| [Group Anagrams](/Python/Strings/groupAnagrams.py) | Group all anagrams in a sublist. |

## Hashing

Use dictionary: key-value pair.

|File Name | Description |
|---|---|
| [Distinct Elements](/Python/Hashing/distinctElements.py) | Count distinct elements in an array. |
| [Non repeating elements](/Python//Hashing/nonRepeatingElement.py) | Return first non repeating element in an array. |
| [Subarray sum zero](/Python/Hashing/subarraySumZero.py) | Check if a subarray exists such that sum of the elements of that subarray = 0. |
| [Pair sum target](/Python/Hashing/pairSumTarget.py) | Return true if you find pair of elements from an array such that their sum is equal to target given. |
| [Distinct element Window](/Python/Hashing/distinctElementWindow.py) | . |
| [Largest consecutive sequence](/Python/Hashing/largestConsecutiveSequence.py) | . |
| [Top k frequent](/Python/Hashing/topKFrequent.py) | . |

## Linked List

Stores collection of data items. Contiguous space is not required.
Items can't be accessed using index.

|File Name | Descripton |
|---|---|
| [Introduction to Node](/Python/LinkedLists/node.py) | Basic introduction to node in linked list. |
| [Linked List](/Python/LinkedLists/LinkedList.py) | Basic implementation of a linked list. |
| [Y Linked List](/Python/LinkedLists/yLinkedList.py) | . |
| [Reverse List](/Python/LinkedLists/reverseList.py) | . |
| [Merge Sorted Linked Lists](/Python/LinkedLists/mergeSortedLL.py) | . |
| [Remove Nth Element from the end](/Python/LinkedLists/removeNthFromEnd.py) | . |
| [Cycle Detection](/Python/LinkedLists/cycleDetection.py) | . |
| [Add two numbers](/Python/LinkedLists/addTwoNumbers.py) | . |

## Stacks

LIFO - Last In, First Out.
Basic APIs:

1. Push
2. Pop
3. Top
4. Size

Wide application: Undo/Redo, Recursion, Paranthesis Balancing, Forward/Back buttons on browser etc.
In python -> easiest implementation way is using lists.

Implementation can be done using Linked List, however, you need to maintain two pointers i.e. head and tail. (Using doubly linked list.)

|File Name | Descripton |
|---|---|
| [Paranthesis Balancing](/Python/Stacks/paranthesisBalancing.py) | Check if the paranthesis are balanced are not. |
| [Reverse paranthesis](/Python/Stacks/reverseParanthesis.py) | Count the number of times you need to reverse paranthesis to balance. |
| [Minimum Stack](/Python/Stacks/minstack.py) | Find minimum element in stack. |
| [Next Greater Element](/Python/Stacks/nextGreaterElement.py) | . |
| [Reverse String](/Python/Stacks/reverseString.py) | Reverse a string using stack. |

## Queues

FIFO - First In, First Out.
Basic APIs:

1. Enqueue/Push
2. Dequeue/Pop
3. Front/Top
4. Size

Wide application: printer queue, downloading queue, message buffers(Kafka, Rabbit MQ), scheduling algorithm, BFS etc.

Python has it's own Queue module. (collection -> deque and queue -> Queue)

**Deque** is a Data Structure which is mixture of stack and queue.

|File Name | Descripton |
|---|---|
| [Introduction to Queue](/Python/Queues/intro_queue.py) | Introduction to queue with a sample usage of it's functions. |
| [Kth Smallest Number](/Python/Queues/kthSmallestNumber.py) | Return kth smallest number that only has digit 2,3. |

## Trees

Hierarchial data structure.

**Binary tree**: Every node of tree can have at max 2 childs.

Traversal Types:

1. Pre order: val, left, right
2. Post order: left, right, val
3. In order: left, val, right

**Note:** Always consider stack space for the space complexity of tree based questions.

|File Name | Descripton |
|---|---|
| [Tree Node](/Python/Trees/treeNode.py) | Basic inroduction to tree. |
| [Traversal in Tree](/Python/Trees/traversal.py) | . |
| [Find Element](/Python/Trees/findElement.py) | . |
| [Identical Trees](/Python/Trees/identical.py) | . |
| [Symmetric Trees](/Python/Trees/symmetric.py) | . |
| [Mirror Tree](/Python/Trees/mirrorTree.py) | . |

## Graphs

Consists of Nodes and Edges.
Types: Directed and Undirected, Weight.

Graph Traversal Algorithms: DFS and BFS.

### Depth First Search

Aggressive algorithm: It will continue down a particular path until it either finds the target or reaches a dead end.
It is a better approach when you need to find path to a given destination asap. However, it does not guarantee to provide you with the shortest path.
Implementation uses stack and dictionary.
Application: pathfinding, scheduling algorithms, assessing investment decision trees, etc.

### Breadth First Search

It's behaviour is called as flood fill because it behaves much like water spreading out over a surface (in unweighted graph).
Always gives shortest path if no edge weights are given.
Implementation uses queue.
Application: GPS, flight reservation systems, peer to peer networks, social media etc.

|File Name | Descripton |
|---|---|
| [Depth First Search](/Python/Graphs/dfs.py) | Implementation of DFS. |
| [Breadth First Search](/Python/Graphs/bfs.py) | Implementation of BFS. |
