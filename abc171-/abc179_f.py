n, q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(q)]

ans = (n - 2)** 2
cnt, wh = [n - 2, n - 2], [[None] * (n - 2), [None] * (n - 2)]
for num, x in query:
    num, x = num - 1, x - 2
    if cnt[num] > x:
        wh[num][x:cnt[num]] = [cnt[1 - num]] * (cnt[num] - x)
        cnt[num] = x
    ans -= wh[num][x]
    wh[num][x] = 0
print(ans)
