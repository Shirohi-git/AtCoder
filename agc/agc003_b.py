n = int(input())
a = [int(input()) for _ in range(n)]

ans, tmp = 0, 0
for ai in a:
    ans += (ai + tmp) // 2
    tmp = (ai + tmp) % 2
    if ai == 0:
        tmp = 0
print(ans)
