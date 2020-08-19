n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for l in range(min(n, k) + 1):
    for r in range(min(n, k) - l + 1):
        bag = sorted(v[:l] + v[n - r:])
        minus = sum(vi for vi in bag[:k - l - r] if vi < 0)
        ans = max(ans, sum(bag) - minus)
print(ans)
