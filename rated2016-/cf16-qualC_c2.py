n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

# 解説AC
ans, frag = 1, 0
for i in range(n):
    if t[i] == a[i] == t[-1] == a[0]:
        frag = 1
    if 0 < i < n - 1 and t[i - 1] == t[i] and a[i] == a[i + 1]:
        ans = ans * min(t[i], a[i]) % mod
print(ans if frag == 1 else 0)
