def bigcmb(N, R):
    if (R < 0) or (N < R):
        return 0
    R = min(R, N - R)
    fact, inv = 1, 1
    for i in range(1, R + 1):
        fact *= N - i + 1
        inv *= i
    return fact // inv


l = int(input())
print(bigcmb(l - 1, 11))
