def main():
    from itertools import accumulate

    acc = [0] + list(accumulate(A))
    plus = [0] + list(accumulate(ai * (ai > 0) for ai in A))

    ans, p_end = 0, plus[-1]
    for r in range(K, N+1):
        l = r - K
        res = max(0, acc[r] - acc[l])
        res += p_end - plus[r] + plus[l]
        ans = max(ans, res)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
