def factorize(N):
    p, PRIME = 2, []
    while p * p <= N:
        while N % p == 0:
            N //= p
            PRIME.append(p)
        p += 1
    if N > 1:
        PRIME.append(N)
    return PRIME


def main():
    prime = factorize(N)
    cnt = 0
    while (1 << cnt) < len(prime):
        cnt += 1
    return print(cnt)


if __name__ == '__main__':
    N = int(input())

    main()
