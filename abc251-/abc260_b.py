def main():
    ans = []

    step1 = sorted((a, -i-1, b) for i, a, b in zip(range(N), A, B))
    ans += [-i for _, i, _ in step1[-X:]] * (X > 0)

    step2 = sorted((b, i, a) for a, i, b in step1[:-X if X > 0 else N])
    ans += [-i for _, i, _ in step2[-Y:]] * (Y > 0)

    step3 = sorted((a+b, i) for b, i, a in step2[:-Y if Y > 0 else N])
    ans += [-i for _, i in step3[-Z:]] * (Z > 0)

    return print(*sorted(ans), sep='\n')


if __name__ == '__main__':
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
