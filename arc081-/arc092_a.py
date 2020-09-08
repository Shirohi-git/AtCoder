n = int(input())
ab = set(tuple(map(int, input().split())) for _ in range(n))
cd = sorted(tuple(map(int, input().split())) for _ in range(n))
ab |= {(-1, -1)}

ans = 0
for c, d in cd:
    tmp = max((b, a) for a, b in ab if (a < c and b < d))
    if tmp != (-1, -1):
        ab.remove(tmp[::-1])
        ans += 1
print(ans)
