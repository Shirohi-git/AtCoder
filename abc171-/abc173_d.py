from collections import deque

n = int(input())
a = sorted(map(int, input().split()), reverse=True)

ans, cnt = 0, deque([a[0]])
for i in a[1:]:
    ans += cnt.popleft()
    cnt.extend([i,i])
print(ans)
