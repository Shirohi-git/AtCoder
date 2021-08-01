from bisect import bisect_left as bi_l


def main():
    ans = 10**9
    for ai in A:
        idx = bi_l(B, ai)
        ans = min(ans, abs(ai-B[idx]), abs(ai-B[idx-1]))
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split())) + [10**10]

    main()
