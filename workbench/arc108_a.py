def makedivisor(N):
    p, upper, lower = 1, [], []
    while p * p <= N:
        if N % p == 0:
            lower.append(p)
            upper.append(N // p)
        p += 1
    return lower, upper

s, p = map(int, input().split())

ans = 0
l, u = makedivisor(p)
for li, ui in zip(l, u):
    ans |= (li + ui == s)
print('Yes' if ans else 'No')
