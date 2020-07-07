from collections import Counter

n = int(input())
s = [Counter(input()) for _ in range(n)]

cnt = s[0]
for scnt in s:
    for str in (scnt | cnt):
        cnt[str] = min(cnt[str], scnt[str])

a = ord('a')
ans = [chr(a + i) * cnt[chr(a + i)] for i in range(26)]
print(*ans, sep='')
