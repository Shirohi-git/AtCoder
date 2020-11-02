n, k = map(int, input().split())

cnt = [0, 0]
for i in range(2, 2 * n + 1):
    cnt.append(min(i - 1, 2 * n - i + 1))

ans = 0
for i in range(2, 2 * n + 1):
    if 0 <= i - k <= 2 * n:
        ans += cnt[i] * cnt[i - k]
print(ans)
