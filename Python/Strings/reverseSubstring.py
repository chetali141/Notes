# Reverse a giving substring

def reverseSubstring(str, start, end):
    l = list(str)
    while start <= end:
        l[start],l[end] = l[end],l[start]
        start += 1
        end -= 1
    answer = ''.join(l)
    return answer

print(reverseSubstring("defabcmno",2,6))
