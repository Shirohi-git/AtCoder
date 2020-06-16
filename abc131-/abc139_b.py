a, b = map(int, input().split())
ans = 0
cnt = 1
while cnt < b:
    ans += 1
    cnt += a-1
print(ans)
