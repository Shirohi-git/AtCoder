x = int(input())
cnt = 100
ans = 0
while cnt < x:
    ans += 1
    cnt = int(cnt*1.01)
print(ans)
