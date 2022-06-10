from itertools import combinations

n = int(input())
s = [input() for _ in range(n)]

cnt = dict({'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0})
for name in s:
    if name[0] in cnt:
        cnt[name[0]] += 1

ans = 0
for i, j, k in combinations(cnt, 3):
    ans += cnt[i] * cnt[j] * cnt[k]
print(ans)
