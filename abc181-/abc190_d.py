def makedivisor(N):
    p, upper, lower = 1, [], []
    while p * p <= N:
        if N % p == 0:
            lower.append(p)
            if p * p != N:
                upper.append(N // p)
        p += 1
    return len(lower + upper)

n = int(input())

while n % 2 == 0:
    n //= 2
print(2 * makedivisor(n))
