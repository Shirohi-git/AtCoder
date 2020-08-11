from bisect import bisect

n = int(input())
ma = [-int(input()) for _ in range(n)]

ans = [1] * n
for ai in ma:
    tmp = bisect(ans, ai)
    ans[tmp] = ai
print(sum(num <= 0 for num in ans))
