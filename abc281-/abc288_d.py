def main():
    acc = [[0] for _ in range(K)]
    for i, ai in enumerate(A):
        acc[i%K].append(acc[i%K][-1] + ai)

    for l, r in LR:
        num = [0] * K
        for li in range(l-1, min(l-1+K, r)):
            num[li%K] -= acc[li%K][li//K]
        for ri in range(max(l-1, r-K), r):
            num[ri%K] += acc[ri%K][ri//K + 1]
        print("Yes" if len(set(num)) == 1 else "No")
    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Q = int(input())
    LR = [list(map(int, input().split())) for _ in range(Q)]

    main()