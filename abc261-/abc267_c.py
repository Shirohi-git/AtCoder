from itertools import accumulate


def main():
    acc = [*accumulate([0]+A)]
    num = sum(i * ai for i, ai in enumerate(A[:M], 1))
    ans = num
    for i, ai in enumerate(A[M:]):
        num -= acc[i+M] - acc[i]
        num += ai*M
        ans = max(ans, num)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
