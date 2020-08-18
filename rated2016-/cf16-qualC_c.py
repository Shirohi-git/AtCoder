n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

ans, l, r = 1, 0, n - 1
for i in range(1, n):
    if t[i] == t[i - 1]:
        ans = ans * t[i] % mod
    if t[i] == a[i]:
        l = i
        break
for i in range(n - 1)[::-1]:
    if a[i] == a[i + 1]:
        ans = ans * a[i] % mod
    if t[i] == a[i]:
        r = i
        break

if not t[l] == max(t) == max(a) == a[r]:
    print(0)
else:
    print(ans * pow(t[l], max(r - l - 1, 0), mod) % mod)
