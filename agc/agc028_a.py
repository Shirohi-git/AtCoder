from math import gcd


def lcm(X, Y):  # 最小公倍数
    return (X * Y) // gcd(X, Y)

n, m = map(int, input().split())
s, t = input(), input()

l = lcm(n, m)
ln, lm = l // n, l // m
if all(s[i // ln] == t[i // lm] for i in range(0, l, lcm(ln, lm))):
    print(l)
else:
    print(-1)
