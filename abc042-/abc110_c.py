from collections import Counter

s, t = input(), input()

d, TorF = {}, True
for si, ti in zip(s, t):
    if ti not in d:
        d[ti] = si
    elif d[ti] != si:
        TorF = False
cnt = Counter(d.values())
TorF = (max(cnt.values()) < 2) & TorF
print('Yes' if TorF else 'No')
