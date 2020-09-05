from collections import Counter

n, p = map(int, input().split())
s = list(map(int, list(input())))

ans = 0
if p in {2, 5}:
    for i, num in enumerate(s):
        if num % p == 0:
            ans += i + 1
else:
    bfo, cnt = 0, [1] + [0] * (p - 1)
    for i, num in enumerate(s[::-1]):
        bfo = (bfo + pow(10, i, p) * num) % p
        ans += cnt[bfo]
        cnt[bfo] += 1
print(ans)
