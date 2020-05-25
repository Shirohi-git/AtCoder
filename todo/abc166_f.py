import sys
input = sys.stdin.readline

n, a, b, c = map(int, input().split())
s = [input().strip() for i in range(n)]

cnt = [0, 0, 0]
ab, ac, bc = 0, 1, 2
for i in s:
    if i == 'AB':
        cnt[ab] += 1
    elif i == 'AC':
        cnt[ac] += 1
    elif i == 'BC':
        cnt[bc] += 1

ans = []
for i in s:
    if i == 'AB':
        cnt[ab] -= 1
        if
        else
    elif i == 'AC':
        cnt[ac] -= 1
        if
        else
    elif i == 'BC':
        cnt[bc] -= 1
        if
        else:
    if a * b * c < 0:
        print('No')
        break

