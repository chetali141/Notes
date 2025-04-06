# Python - Notes

The repository contains some of the Python - DSA programming codes.

## Basic Questions

|File Name | Descripton |
|---|---|
| [Design Patterns](/Python/DesignPatterns.py) | The file contains code for some basic design patterns asked to print using loops. |
| [Password Generator](/Python/PasswordGenerator.py) | This file contains a program which can generate password for you or secure your password. |
| [Tower of Hanoi](/Python/TowerOfHanoi.py) | This file contains the solution to the Tower of Hanoi mathematical puzzle. |
| [Palindrome Number](/Python/PalindromeNumber.py) | This file contains the solution to the palindrome problem. |
| [Pascal's Triangle](/Python/PascalTriangle.py) | In the Pascal's triangle, each number is the sum of the two numbers directly above it. This file contains the code to generate Pascal's triangle. |
| [Binary Search](/Python/binarySearch.py) | Use binary search to find an elements. |

## Arrays

|File Name | Descripton |
|---|---|
| [Reverse Array](/Python/Arrays/reverseArray.py) | Reverse the given array without using extra space. |
| [Rotate Array](/Python/Arrays/rotateArray.py) | Rotate a given array from left to right 'k' times without using extra space. |
| [Sum of all elements between range](/Python/Arrays/sumBtwLandR.py) | Calculate sum of all the elements of the array present between the given left and right index. |
| [Equilibrium Index](/Python/Arrays/equilibriumIndex.py) | Find the equilibrium index 'i' such that the sum of all elements on it's left is equal to the sum of all the elements on it's right. |
| [Pick from both sides](/Python/Arrays/pickFromBothSides.py) | Pick 'k' elements from left or right or both the sides of the array to find the maximum sum. |
| [Sum of all odd or even elements between range](/Python/Arrays/sumRangeOddEven.py) | Calculate sum of all elements present on odd or even index between the given range from left to right. |
| [Leader Element](/Python/Arrays/leaders.py) | Find the leader element in the given array. A element is leader if it is strictly greater than all the elements to its right. |
| [Closest Min Max](/Python/Arrays/closestMinMax.py) | Given an array, find the smallest continuous part of the array such that it contains the minimum and maximum values of the array. |
| [Subarray](/Python/Arrays/subarray.py) | Print all the subarrays. |
| [Subarray of length k](/Python/Arrays/subarrayK.py) | Generate all subarrays of length 'k' in a given array. |
| [Maximum subarray sum](/Python/Arrays/maxSubarraySum.py) | Return the maximum sum from the sum of all subarrays present within a given array. |
| [Maximum subarray sum of length k](/Python/Arrays/maxSubarraySumK.py) | Return maximum sum from sum of all subarrays of length 'k' present within a given array. |
| [Sum of all subarray sum](/Python/Arrays/allSubarraySum.py) | Given an array, find the sum of all subarray sum. |
| [All diagonals of a square matrix](/Python/Arrays/diagonalSquare.py) | Print all diagonals in a square matrix. |
| [Product Except Self](/Python/Arrays/productExceptSelf.py) | Given an array, find product of all elements in array except self. |
| [Peak Element](/Python/Arrays/peakElement.py) | A peak element is an element that is strictly greater than its neighbors Given an integer array, find a peak element, and return its index. |

## Strings

|File Name | Description |
|---|---|
| [Count Pairs](/Python/Strings/countPairs.py) | Given string 's', count the number of pairs such that: i < j, s[i] = 'a' and s[j] = 'g'. |
| [Sort Lowercase](/Python/Strings/sortLowercase.py) | Given a string in lowercase, sort it into asc order. |
| [Reverse Substring](/Python/Strings/reverseSubstring.py) | Reverse a given substring in a string. |
| [Valid Palindrome](/Python/Strings/validPalindrome.py) | Given a string s, return true if it is a palindrome, otherwise return false. Consider it to be case-insensitive and ignore all non-alphanumeric characters. |
| [Valid Palidrome Substring](/Python/Strings/validPalindromeSubstring.py) | Given a string 'str', find the length of longest palindromic substring. |
| [Group Anagrams](/Python/Strings/groupAnagrams.py) | Group all anagrams in a sublist. |

## Hashing

Use dictionary: key-value pair.

|File Name | Description |
|---|---|
| [Distinct Elements](/Python/Hashing/distinctElements.py) | Count distinct elements in an array. |
| [Non repeating elements](/Python//Hashing/nonRepeatingElement.py) | Return first non repeating element in an array. |
| [Subarray sum zero](/Python/Hashing/subarraySumZero.py) | Check if a subarray exists such that sum of the elements of that subarray = 0. |
| [Pair sum target](/Python/Hashing/pairSumTarget.py) | Return true if you find pair of elements from an array such that their sum is equal to target given. |
| [Distinct element Window](/Python/Hashing/distinctElementWindow.py) | Given N elements in an array, calculate distinct number of elements in window of length 'k'. |
| [Largest consecutive sequence](/Python/Hashing/largestConsecutiveSequence.py) | Given an array, find the largest sequence which can be rearranged to form a sequence of consecutive numbers. |
| [Top k frequent](/Python/Hashing/topKFrequent.py) | Given an integer array nums and an integer k, return the k most frequent elements within the array. |

## Linked List

Stores collection of data items. Contiguous space is not required.
Items can't be accessed using index.

|File Name | Descripton |
|---|---|
| [Introduction to Node](/Python/LinkedLists/node.py) | Basic introduction to node in linked list. |
| [Linked List](/Python/LinkedLists/LinkedList.py) | Basic implementation of a linked list. |
| [Y Linked List](/Python/LinkedLists/yLinkedList.py) | Given 2 head pointers of a linked list, find if both the linkedlist intersect or not. |
| [Reverse List](/Python/LinkedLists/reverseList.py) | Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list. |
| [Merge Sorted Linked Lists](/Python/LinkedLists/mergeSortedLL.py) | Given the heads of two sorted linked lists, merge the two lists into one sorted list. |
| [Remove Nth Element from the end](/Python/LinkedLists/removeNthFromEnd.py) | Given the head of a linked list, remove the nth node from the end of the list and return its head. |
| [Cycle Detection](/Python/LinkedLists/cycleDetection.py) | Given the head of a linked list, determine if the linked list has a cycle in it. |
| [Add two numbers](/Python/LinkedLists/addTwoNumbers.py) | . |

## Stacks

LIFO - Last In, First Out.
Basic APIs:

1. Push
2. Pop
3. Top
4. Size

Application: Undo/Redo, Recursion, Paranthesis Balancing, Forward/Back buttons on browser etc.
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

Application: printer queue, downloading queue, message buffers(Kafka, Rabbit MQ), scheduling algorithm, BFS etc.

Python has it's own Queue module. (collection -> deque and queue -> Queue).
**Deque** is a Data Structure which is mixture of stack and queue.

### Priority Queue

It is useful when resources needs to be allocated based on some rules or precedence. The highest priority element is removed first.
Basic APIs:

1. Get - Fetch the one with the highest priority
2. Put - Add element in the queue
3. is_empty

Application: AI(A* search algorithm), optimzation algorithms, spam filtering, OS process scheduling etc.

|File Name | Descripton |
|---|---|
| [Introduction to Queue](/Python/Queues/intro_queue.py) | Introduction to queue with a sample usage of it's functions. |
| [Kth Smallest Number](/Python/Queues/kthSmallestNumber.py) | Return kth smallest number that only has digit 2,3. |
| [Introduction to Priority Queue](/Python/Queues/priorityQueue.py) | Introduction to priority queue. |

## Trees

Hierarchial data structure.

**Binary tree**: Every node of tree can have at max 2 childs.

**Traversal Types**: Three types of tree traversal.

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

It's behaviour is called as **flood fill** because it behaves much like water spreading out over a surface (in unweighted graph).
Always gives shortest path if no edge weights are given.
Implementation uses queue.
Application: GPS, flight reservation systems, peer to peer networks, social media etc.

### A* Search Algorithm

Widely used algorithm for calculating shortest paths. The rule of thumb or heuristics is to chosse the next position based on the distance from the goal.
**The Manhattan Distance or Taxi Cab Distance**: used to calculate the distance between 2 points on 2D grid following the grid layout. Concept behind: Taxi needs to stay on road and can't drive through buildings.
**Eucledian Distance**: calculates distance using Pythagoras Theorm.
Application: GPS, NLP, ML, Puzzle problems, Video games, Robotics etc.

Key Values:

1. G value: best distance from start to current cell
2. H value: heuristic distance from current cell to destination
3. F value: sum of G and H value

|File Name | Descripton |
|---|---|
| [Depth First Search](/Python/Graphs/dfs.py) | Implementation of DFS. |
| [Breadth First Search](/Python/Graphs/bfs.py) | Implementation of BFS. |
| [A* Search Algorithm](/Python/Graphs/aStar.py) | Implementation of A* search algorithm. |
