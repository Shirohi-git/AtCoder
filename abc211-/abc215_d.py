def main():
    def factorize(N):
        p, PRIME = 2, []
        while p * p <= N:
            while N % p == 0:
                N //= p
                PRIME.append(p)
            p += 1
        if N > 1:
            PRIME.append(N)
        return set(PRIME)

    p_set = set()
    for ai in A:
        p_set |= factorize(ai)

    bit = [1] * (M+1)
    bit[0] = 0
    for pi in p_set:
        for i in range(pi, M+1, pi):
            bit[i] = 0
    ans = [sum(bit)] + [i for i in range(M+1) if bit[i]]
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
