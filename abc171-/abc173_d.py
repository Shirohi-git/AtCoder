n = int(input())
a = sorted(map(int, input().split()))[::-1]

ans, que = 0, [a[0]]
for i, ai in enumerate(a[1:]):
    ans += que[i]
    que += [ai, ai]
print(ans)
