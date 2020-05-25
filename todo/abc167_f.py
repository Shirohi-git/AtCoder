import sys

n = int(input())
s = [list(input()) for i in range(n)]

s_cnt, s_minmax = [0] * n, [[0, 0] for i in range(n)]
for i in range(n):
    for j in s[i]:
        if j == '(':
            s_cnt[i - 1] += 1
            s_minmax[i-1][1] = max(s_minmax[i-1][1], s_cnt[i - 1])
        else:
            s_cnt[i - 1] -= 1
            s_minmax[i-1][1] = max(s_minmax[i-1][1]-1, 0)
            s_minmax[i-1][0] = min(s_minmax[i-1][0], s_cnt[i - 1])

s_minmax.sort(reverse=True)
if sum(s_cnt) != 0:
    print('No')
    exit()

print(s_minmax)
right = 0
for list in s_minmax:
    l, r = list
    right += l
    if right < 0:
        print('No')
        exit()
    right += r
else:
    print('Yes')
