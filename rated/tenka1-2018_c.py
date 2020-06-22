n = int(input())
a = sorted([int(input()) for _ in range(n)])

if n % 2 == 0:
    ans = 2 * (sum(a[n // 2:]) - sum(a[:n // 2]))
    ans += a[n // 2 - 1] - a[n // 2]
    print(ans)
elif n % 2 == 1:
    ans = 2 * (sum(a[n // 2 + 1:]) - sum(a[:n // 2]))
    print(max(ans + a[n // 2] - a[n // 2 + 1],
              ans - a[n // 2] + a[n // 2 - 1]))
