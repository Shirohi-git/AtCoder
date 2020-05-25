from itertools import combinations

n, x, y = map(int, input().split())

cnt = [0] * n
for i, j in combinations(range(1, n + 1), 2):
    dist = min(abs(j - i), abs(i - x) + abs(j - y) + 1,
               abs(i - y) + abs(j - x) + 1)
    cnt[dist] += 1

for i in range(1, n):
    print(cnt[i])
