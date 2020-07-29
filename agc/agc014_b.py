from collections import defaultdict

n, m = map(int, input().split())
ab = (list(map(int, input().split())) for _ in range(m))

cnt = defaultdict(int)
for a, b in ab:
    cnt[a] += 1
    cnt[b] += 1
ans = all(cnt[i] % 2 == 0 for i in cnt)
print('YES' if ans else 'NO')
