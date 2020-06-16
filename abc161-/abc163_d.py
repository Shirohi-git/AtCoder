n, k = map(int, input().split())
mod = 10 ** 9 + 7

cnt = 0
L, R = 0, 0
for i in range(k-1):
    L += i
    R += n - i

for i in range(k-1, n+1):
    L += i
    R += n - i
    cnt += R - L + 1
print(cnt % mod)
