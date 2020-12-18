n = int(input())
c = [int(input()) for _ in range(n)]

flag = [0] * n
res, now = 1, 0
while res:
    now = c[now] - 1
    if flag[now] or now == 1:
        res -= (res + 1) * flag[now]
        break
    flag[now] = 1
    res += 1
print(res)
