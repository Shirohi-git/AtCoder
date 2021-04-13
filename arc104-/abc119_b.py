n = int(input())
xu = [input().split() for _ in range(n)]
xu = [[int(x.replace('.', '')), u] for x, u in xu]

ans = [0, 0]
for x, u in xu:
    if u == 'JPY':
        ans[0] += x
    if u == 'BTC':
        ans[1] += x * 38
ans[1] /= 10 ** 4
print(sum(ans))
