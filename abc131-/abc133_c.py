l, r = map(int, input().split())
ans = 2019
cnt = min(l + 2019, r)
for i in range(l, cnt):
    for j in range(i + 1, cnt + 1):
        ans = min(ans, i*j % 2019)
print(ans)
