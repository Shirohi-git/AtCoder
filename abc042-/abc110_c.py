from collections import Counter

s, t = input(), input()

dict = {}
for si, ti in zip(s, t):
    if ti not in dict:
        dict[ti] = si
    elif dict[ti] != si:
        print('No')
        break
else:
    cnt = Counter(dict.values())
    bool = all(cnt[i] <= 1 for i in cnt)
    print('Yes' if bool else 'No')
