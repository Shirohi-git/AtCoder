from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = deque([])

for i, ai in enumerate(a):
    if i % 2 == 0:
        b.append(ai)
    elif i % 2 == 1:
        b.appendleft(ai)
b = list(b)
print(*(b if n % 2 == 0 else b[::-1]))
