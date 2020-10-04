from collections import defaultdict

n, s = input().split()

ans, at, cg = 0, 0, 0
cnt = defaultdict(int)
cnt[(0, 0)] = 1
for si in s:
    at += (si == 'A') - (si == 'T')
    cg += (si == 'C') - (si == 'G')
    ans += cnt[(at, cg)]
    cnt[(at, cg)] += 1
print(ans)
