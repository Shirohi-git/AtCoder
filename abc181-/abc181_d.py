from collections import Counter

s = input()

cnt = Counter(s)
ans, flen = 0, min(3, len(s))
for i in range(125):
    num = Counter(str(i * 8).zfill(flen))
    ans |= 1 - bool(num - cnt)
print('Yes' if ans else 'No')
