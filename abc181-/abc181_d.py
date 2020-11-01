from collections import Counter

s = input()

cnt, flen = Counter(s), min(3, len(s))
num = [Counter(str(i).zfill(flen)) for i in range(0, 10 ** flen, 8)]

ans = 0
for d in num:
    ans += all(cnt[k] >= d[k] for k in d)
print('Yes' if ans > 0 else 'No')
