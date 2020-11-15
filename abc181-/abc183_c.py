from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for l in permutations(range(1, n), n - 1):
    l = list(l) + [0]
    time, i = 0, 0
    for j in l:
        time += t[i][j]
        i = j
    ans += (time == k)
print(ans)
