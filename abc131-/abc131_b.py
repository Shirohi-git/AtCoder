n, l = map(int, input().split())
cnt = float('inf')
for i in range(n):
    if cnt > abs(l + i):
        ans, cnt = l + i, abs(l + i)

print(n*(l-1)+n*(n+1)//2-ans)
