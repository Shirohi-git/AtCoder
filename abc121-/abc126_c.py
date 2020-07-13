from math import ceil, log2

n, k = map(int, input().split())

rate = 0
for i in range(1, n + 1):
    cnt = 0
    if i < k:
        cnt = ceil(log2(k) - log2(i))
    rate += 1 / n * 0.5 ** cnt

print(rate)
