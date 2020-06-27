n = int(input())

ans = 0
for i in range(1, n + 1):
    cnt = n // i
    ans += i * cnt * (cnt + 1) // 2
print(ans)
