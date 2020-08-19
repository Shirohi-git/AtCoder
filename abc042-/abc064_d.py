from collections import deque

n = int(input())
s = input()

l, que = 0, deque([])
for i in s:
    que.append(i)
    if i == '(':
        l += 1
    elif i == ')':
        if l == 0:
            que.appendleft('(')
            l += 1
        l -= 1
print(*que, ')' * l, sep='')
