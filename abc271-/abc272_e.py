def main():
    num = [[] for _ in range(M)]
    for i, ai in enumerate(A, 1):
        if ai >= N:
            continue
        l = max(1, (-ai)//i)
        r = min(M, (N-ai)//i)
        for j in range(l, r+1):
            if 0 <= ai + i*j < N:
                num[j-1] += [ai + i*j]

    ans = []
    for ni in map(sorted, num):
        res = 0
        for nij in ni:
            res += (res == nij)
        ans.append(res)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    main()
