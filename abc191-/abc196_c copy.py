n = int(input())

lst = [pow(10, i + 1) for i in range(7)]
ans = 0
for i in lst:
    if i ** 2 // 10 <= n < i ** 2:
        ans += n // i
        ans -= (n // i > n % i)
    ans += (i - 1) * (n >= i ** 2)
    ans -= (i // 10 - 1) * (i ** 2 // 10 <= n)
print(ans)
