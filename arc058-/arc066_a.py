from collections import Counter

n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

cnt = Counter(a)
if any(n % 2 == i % 2 for i in cnt):
    print(0); exit()
if any(cnt[i] != 2 for i in cnt if i != 0):
    print(0); exit()
print(pow(2, n // 2, mod))
