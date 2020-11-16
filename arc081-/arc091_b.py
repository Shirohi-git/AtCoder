n, k = map(int, input().split())

cnt = 0
for b in range(k + 1, n + 1):
    cnt += (n // b) * (b - k)
    cnt += max(0, n % b - max(k - 1, 0))
print(cnt)
