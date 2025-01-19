"""
Reverse a given string using Stack.
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def reverse_string(my_string):
    
    reversed_string = ""

    str_stack = Stack()

    for c in my_string:
        str_stack.push(c)

    while str_stack.is_empty()==False:
        c = str_stack.pop()
        reversed_string += c

    return reversed_string

# print(reverse_string(".kcatS fo noitseuq a si sihT"))
