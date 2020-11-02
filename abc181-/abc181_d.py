from collections import Counter

s = input()

cnt, flen = Counter(s), min(3, len(s))
num = [Counter(str(i * 8).zfill(flen)) for i in range(10 ** flen)]

ans = 0
for d in num:
    ans |= all(cnt[k] >= d[k] for k in d)
print('Yes' if ans else 'No')
