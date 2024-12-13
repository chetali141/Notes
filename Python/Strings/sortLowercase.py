# Given a string in lowercase, sort it into asc order --> This is known as count sort

def sortLowercase(str):
    answer = ''
    l = [0] * 26
    for c in str:
        l[ord(c)-97] += 1
    for i in range(26):
        answer = answer + chr(i+97)*l[i]
    return answer

print(sortLowercase("dcabbacd"))
