def main():
    dic = [[] for _ in range(K)]
    for i in range(N):
        dic[i % K].append(A[i])
    dic = [sorted(di) for di in dic]

    bfo, res = 0, 1
    for ij in range(N):
        i, j = divmod(ij, K)
        res &= (bfo <= dic[j][i])
        bfo = dic[j][i]
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
