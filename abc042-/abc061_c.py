n, k = map(int, input().split())
ab = sorted(list(map(int, input().split())) for _ in range(n))

for a, b in ab:
    k -= b
    if k <= 0:
        print(a)
        break
