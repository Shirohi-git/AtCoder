from bisect import bisect


def main():
    a = [-10**10] + A + [10**10]
    for bi in B:
        idx = bisect(a, bi)
        print(min(a[idx] - bi, bi - a[idx-1]))
    return None


if __name__ == '__main__':
    N = int(input())
    A = sorted(map(int, input().split()))
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    main()
