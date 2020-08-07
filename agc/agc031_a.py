from collections import Counter

n = int(input())
s = Counter(input())
mod = 10 ** 9 + 7

ans = 1
for i in s.values():
    ans = ans * (i + 1) % mod
print(ans - 1)
