from math import gcd


t = 1
nsk = [list(map(int, input().split())) for _ in range(t)]

for n, s, k in nsk:
    res, ans = 1, 1
    while (n - s) % k > 0:
        ans *= n // k + 1
        if n % k == 0:
            res = 0
            break
        k = min(k - n % k, n % k)

        s = (s + k) % n
        print(k, s)
    ans *= (n - s) // k
    print(ans if res else - 1)


