n = int(input())

ans = 0
for i in range(1, int(n ** 0.5) + 1):
    m = n // i - 1
    if m > 0 and n % i == 0 and n // m == n % m:
        ans += m
print(ans)
