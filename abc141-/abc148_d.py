n = int(input())
a = list(map(int, input().split()))

ans, cnt = 0, 1
for i in a:
    if i == cnt:
        cnt += 1
    else:
        ans += 1
print(-1 if ans == n else ans)
