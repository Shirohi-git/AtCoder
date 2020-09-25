n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = pow(10, 9)
for i in range(n - k + 1):
    tmp = min(abs(x[i]), abs(x[i + k - 1]))
    ans = min(ans, tmp + x[i + k - 1] - x[i])
print(ans)
