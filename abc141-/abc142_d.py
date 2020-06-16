a, b = map(int, input().split())


def prime_factorize(n):
    ans = []
    while n % 2 == 0:
        ans.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            ans.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        ans.append(n)
    return ans


cnt = list(set(prime_factorize(a)) & set(prime_factorize(b)))
print(len(cnt)+1)
