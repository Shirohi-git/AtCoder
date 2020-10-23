n, k = map(int, input().split())

cnt = n * (n - 1) // 2 - k
print(-1 if n - 1 > cnt else cnt)

cnt *= (n - 1 <= cnt)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if cnt > 0:
            print(i, j)
            cnt -= 1
