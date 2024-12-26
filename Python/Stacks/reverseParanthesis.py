"""
Given even length sequence of paranthesis containing '(' and ')'.
Return min no of time you have to reverse a paranthesis to make the whole sequence balanced. 
"""

def reverseParanthesis(str):

    open = "("
    close = ")"

    stack = []

    for i in str:
        if i == open:
            stack.append(i)
        elif i == close:
            if len(stack) > 0 and stack[len(stack) - 1] == open:
                stack.pop()
            else:
                stack.append(i)
        print(stack)

    return len(stack)

print(reverseParanthesis("())(()"))
print(reverseParanthesis(")("))
print(reverseParanthesis(")(())((("))
