n = int(input())
p = list(map(int, input().split()))

ans = n
cnt = n+1
for i in range(n):
    if cnt < p[i]:
        ans -= 1
    cnt = min(cnt, p[i])


print(ans)
