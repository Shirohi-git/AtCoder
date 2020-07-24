n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

# 解説AC
ans, num = 0,1
for i in range(60):
    cnt = sum((ai & num) >> i for ai in a)
    ans += (cnt * (n - cnt) * num) % mod
    num <<= 1
print(ans % mod)
