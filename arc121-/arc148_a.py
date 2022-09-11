from math import gcd


def main():
    g = 0
    for ai, aj in zip(A, A[1:]):
        g = gcd(g, aj-ai)
    g = max(2, g)
    a = [ai % g for ai in A]
    ans = min(2, len(set(a)))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = sorted(map(int, input().split()))

    main()
