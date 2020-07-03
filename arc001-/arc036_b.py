n = int(input())
h = [int(input()) for _ in range(n)]

ans, s = 1, 0
for i in range(1, n - 1):
    if h[i - 1] > h[i] < h[i + 1]:
        u = i
        ans = max(ans, u - s + 1)
        s = i
print(max(ans, (n - 1) - s + 1))
