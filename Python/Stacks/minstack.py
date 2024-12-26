"""
Return the min of all the elements present in the stack in O(1)
"""

class Stack:

    stack = []
    min = []

    def push(self,num):
        if len(self.stack) == 0 and len(self.min) == 0:
            self.min.append(num)
        elif num < self.min[len(self.min) - 1]:
            self.min.append(num)
        else:
            self.min.append(self.min[len(self.min)-1])
        self.stack.append(num)

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def getMin(self):
        return self.min[len(self.min) - 1]    

stack = Stack()

stack.push(12)
stack.push(6)
stack.push(13)
stack.push(5)
stack.push(10)
stack.push(1)
stack.push(5)
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
