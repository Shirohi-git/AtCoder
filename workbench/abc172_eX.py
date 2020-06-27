n, m = map(int, input().split())
mod = 10 ** 9 + 7

cnt = 1
for i in range(n):
    cnt = cnt * (m - i) % mod

