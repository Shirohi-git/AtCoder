n = int(input())
a = list(map(int, input().split()))

ans, cnt, node = 0, sum(a), 1
for i in range(n + 1):
    ans += node
    cnt -= a[i]
    node = min(cnt, (node - a[i]) * 2)
    if node < 0:
        print(-1)
        break
else:
    print(ans)
