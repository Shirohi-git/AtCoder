n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 10 ** 6
for i in range(n):
    for j in range(n):
        if i == j:
            ans = min(sum(ab[i]), ans)
        else:
            ans = min(max(ab[i][0], ab[j][1]), ans)
print(ans)
