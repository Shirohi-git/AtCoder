from math import gcd

n, m = map(int, input().split())
a = list(map(lambda x: int(x) // 2, input().split()))

pow2, min_a = 1, min(a)
while min_a % 2 == 0:
    pow2 *= 2
    min_a //= 2

ans = 1
for ai in a:
    ans *= (ai // pow2) % 2
    ans = (ans * ai) // gcd(ans, ai)
print((m // ans + 1) // 2 if ans > 0 else ans)
