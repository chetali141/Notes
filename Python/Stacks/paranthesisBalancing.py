"""
Tell if the sequence of paranthesis is balanced or not.
eg: 
(())()(((()))) -> balanced
([{]}) -> not balanced
"""

def paranthesisBalancing(str):
    open = ["(","[","{"]
    close = [")","]","}"]

    stack = []

    for i in str:
        if i in open:
            stack.append(i)
        elif i in close:
            posn = close.index(i)
            if len(stack) > 0 and open[posn] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False

    if len(stack) > 0:
        return False
    else:
        return True


print(paranthesisBalancing("(())()(((())))"))
print(paranthesisBalancing("([{]})"))
