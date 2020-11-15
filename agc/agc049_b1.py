from collections import deque

n = int(input())
s, t = input(), input()

tque = deque([])
ans, sbfo = 0, -1
for i in range(n):
    if int(t[i]):
        tque.append(i)
    if int(s[i]):
        if tque and sbfo < 0:
            ans += i - tque.popleft()
        else:
            ans += (i - sbfo) * (sbfo >= 0)
            sbfo = (i + 1) * (sbfo < 0) - 1
print(-1 if sbfo >= 0 or tque else ans)
