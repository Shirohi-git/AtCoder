def makedivisor(N):  # 約数列挙
    p, upper, lower = 1, [], []
    while p * p <= N:
        if N % p == 0:
            lower.append(p)
            if p * p != N:
                upper.append(N // p)
        p += 1
    return lower + upper[::-1]


def totient(N):  # オイラーのトーシェント関数
    p, phi = 2, N
    while p * p <= N:
        if N % p == 0:
            phi = phi // p * (p - 1)
        while N % p == 0:
            N //= p
        p += 1
    if N > 1:
        phi = phi // N * (N - 1)
    return phi


k = int(input()) * 9

# 解説AC オイラーの定理 O(n**0.5 * logn)
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()
if k % 7 == 0:
    k //= 7

cnt = totient(k)
num = makedivisor(cnt)
for i in num:
    if pow(10, i, k) == 1:
        print(i)
        break
