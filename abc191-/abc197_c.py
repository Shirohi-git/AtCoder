from itertools import product

n = int(input())
a = list(map(int, input().split()))

ans = 2e31 - 1
for com in product([0, 1], repeat=n - 1):
    res, num = 0, a[0]
    for ai, bit in zip(a[1:], list(com)):
        if bit:
            num |= ai
        else:
            res ^= num
            num = ai
    ans = min(ans, res ^ num)
print(ans)
