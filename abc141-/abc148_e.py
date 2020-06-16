n = int(input())

ans, tmp = 0, 5
if n % 2 == 0:
    n //= 2
    while tmp <= n:
        ans += n // tmp
        tmp *= 5
print(ans)
