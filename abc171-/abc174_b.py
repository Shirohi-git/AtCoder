n, d = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for p, q in pq:
    ans += (p ** 2 + q ** 2 <= d ** 2)
print(ans)
