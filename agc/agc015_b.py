s = str(input())

n, cnt = len(s), 0
for i, ud in enumerate(s):
    i = i + 1
    if ud == 'U':
        cnt += (n - i) + 2 * (i - 1)
    if ud == 'D':
        cnt += 2 * (n - i) + (i - 1)
print(cnt)
