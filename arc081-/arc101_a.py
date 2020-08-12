n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10 ** 9
for i in range(n - k + 1):
    x1, xk = x[i], x[i + k - 1]
    if x1 * xk >= 0:
        t = max(abs(x1),abs(xk))
    elif x1 * xk < 0:
        t = min(abs(x1), abs(xk)) + abs(x1 - xk)
    ans = min(ans, t)
print(ans)
