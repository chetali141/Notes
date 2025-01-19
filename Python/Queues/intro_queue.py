"""
Introduction to Queue: using deque module from collections package
"""
from collections import deque

# Creating class Queue
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

# transform the initial queue, represented by:
# ['wore', 'a', 'silly', 'hat', 'the', 'aardvark']
# into the correct solution:
# deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])

def queue_challenge():
    my_queue = Queue()
    word_list =  ["wore", "a", "silly", "hat", "the", "aardvark"]
    for word in word_list:
        my_queue.enqueue(word)

    my_queue.enqueue(my_queue.dequeue())
    my_queue.enqueue(my_queue.dequeue())
    my_queue.enqueue(my_queue.dequeue())
    my_queue.enqueue(my_queue.dequeue())

    return my_queue.items

print(queue_challenge())
