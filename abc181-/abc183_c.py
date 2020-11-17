from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for l in permutations(range(1, n), n - 1):
    time, i = 0, 0
    for j in l:
        time += t[i][j]
        i = j
    time += t[i][0]
    ans += (time == k)
print(ans)
