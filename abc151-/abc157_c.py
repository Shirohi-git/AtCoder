import sys
n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]

ans = [-1] * n
for i in sc:
    s, c = i
    if (ans[s-1] == c) | (ans[s-1] == -1):
        ans[s-1] = c
    else:
        print(-1)
        sys.exit()

for i in range(n):
    if ans[i] == -1:
        if (i == 0) & (n != 1):
            ans[i] = 1
        else:
            ans[i] = 0

if n != 1:
    if ans[0] == 0:
        print(-1)
        sys.exit()

print(*ans, sep='')
