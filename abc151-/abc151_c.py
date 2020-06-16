import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p_s = [list(map(str, input().split())) for _ in range(m)]

ac = [0 for _ in range(n)]
wa = [0 for _ in range(n)]

for i in range(m):
    if p_s[i][1] == 'WA':
        if ac[int(p_s[i][0]) - 1] == 0:
            wa[int(p_s[i][0]) - 1] += 1
    else:
        ac[int(p_s[i][0]) - 1] = 1

for i in range(n):
    if ac[i] == 0:
        wa[i]=0

print(sum(ac), sum(wa))
