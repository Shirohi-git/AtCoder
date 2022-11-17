def main():
    ans = SUM
    cnt, bfo = 0, A[0]
    for ai in A*2:
        if not (bfo == ai or (bfo+1) % M == ai):
            cnt = 0
        cnt, bfo = cnt+ai, ai
        ans = min(ans, SUM-cnt)
    return print(max(ans, 0))


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    SUM = sum(A)

    main()
