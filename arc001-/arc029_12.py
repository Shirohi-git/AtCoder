from itertools import product

n = int(input())
t = [int(input()) for _ in range(n)]

sumt = sum(t)
ans = sumt
for c in product([0, 1], repeat=n):
    cnt = sum(ti * ci for ti, ci in zip(t, c))
    ans = min(ans, max(sumt - cnt, cnt))
print(ans)
