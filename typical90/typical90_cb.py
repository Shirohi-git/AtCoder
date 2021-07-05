from itertools import product


def main():
    ans = 0
    for bit in product([0, 1], repeat=N):
        b, cnt = 0, D
        for ai, bi in zip(A, bit):
            b |= (ai if bi else 0)
        for i in range(D):
            cnt -= ((b >> i) & 1)
        ans += pow(-1, sum(bit)) * pow(2, cnt)
    return print(ans)


if __name__ == '__main__':
    N, D = map(int, input().split())
    A = list(map(int, input().split()))

    main()
