s = input()

cnt = [1, 1, 1, 1]
for si in s:
    cnt['NWSE'.index(si)] = 0
res = any(cnt[i] ^ cnt[i + 2] for i in [0, 1])
print('Yes' if 1 - res else 'No')
