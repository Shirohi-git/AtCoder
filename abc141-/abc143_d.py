from bisect import bisect

n = int(input())
l = sorted(map(int, input().split()))
linv = l[::-1]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x = linv[i] - linv[j]
        ans += max((n - j - 1) - bisect(l, x), 0)
print(ans)
