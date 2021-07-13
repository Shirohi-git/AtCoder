def main():

    def make_UpTriMat(mat):
        n, m = len(mat), len(mat[0])
        res, col = [mi[:] for mi in mat], []
        rank = 0
        for i in range(m):
            if all(res[j][i] == 0 for j in range(rank, n)):
                continue

            col.append(i)
            for j in range(rank, n):
                if res[j][i]:
                    res[rank], res[j] = res[j][:], res[rank][:]
                    break
            for j in range(rank+1, n):
                if res[j][i]:
                    res[j] = [rjk ^ rrk for rjk, rrk in zip(res[j], res[rank])]
            rank += 1

        return res, col

    a, idx = make_UpTriMat(A)
    s = S[:]
    for ai, id in zip(a, idx):
        if s[id]:
            s = [aij ^ sj for aij, sj in zip(ai, s)]
    ans = pow(2, len(a) - len(idx), MOD9)
    return print(0 if sum(s) else ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        _ = input()
        for j in map(int, input().split()):
            A[i][j-1] = 1
    S = list(map(int, input().split()))
    MOD9 = 998244353

    main()
