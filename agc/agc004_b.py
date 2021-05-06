n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 10e15
cost = a[:n]
for i in range(n):
    cost = [min(cj, a[j-i]) for j, cj in enumerate(cost)]
    ans = min(ans, sum(cost) + x*i)
print(ans)
