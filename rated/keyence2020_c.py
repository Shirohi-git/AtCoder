n, k, s = list(map(int, input().split()))
ans = [None for _ in range(n)]

for i in range(k):
    ans[i] = s
for i in range(k, n):
    if s == 1:
        ans[i] = 2
    else:
        ans[i] = s//2+1

print(*ans)
