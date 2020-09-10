x = int(input())
cnt, ans = 100, 0
while cnt < x:
    ans += 1
    cnt = cnt * 101 // 100
print(ans)
