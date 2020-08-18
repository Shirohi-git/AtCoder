n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

# 解説AC
if n <= 2:
    print(int(t == a))
    exit()

ans = 1
for i in range(1, n - 1):
    if ((t[i - 1] < t[i] and t[i] > a[i])
        or (a[i] > a[i + 1] and t[i] < a[i])):
            print(0)
            break
    elif t[i - 1] == t[i] and a[i] == a[i + 1]:
        ans = ans * min(t[i], a[i]) % mod
else:
    print(ans)
