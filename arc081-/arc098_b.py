n = int(input())
a = list(map(int, input().split()))

ans, xor, cnt = 0, 0, 0
for i in range(n):
    while cnt < n and xor & a[cnt] == 0:
        xor ^= a[cnt]
        cnt += 1
    ans += cnt - i
    xor ^= a[i]
print(ans)
