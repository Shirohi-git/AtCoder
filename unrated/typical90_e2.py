def mat_product(a, b):
    n, m, l = len(a), len(b), len(b[0])
    res = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD1
    return res


def mat_powlst(cnt, mat):
    n = len(mat)
    res = [[[0] * n for _ in range(n)] for _ in range(cnt+1)]
    res[0] = [[matij for matij in mati] for mati in mat]

    for i in range(cnt):
        res[i+1] = mat_product(res[i], res[i])
    return res


def main():
    n, b, k = map(int, input().split())
    c = list(map(int, input().split()))

    if b > 31:
        exit()

    # 小課題2 行列累乗 O(b3 logn)
    mat = [[0] * b for _ in range(b)]
    for i in range(b):
        for cj in c:
            mat[i][(i*10 + cj) % b] += 1
    pow_lst = mat_powlst(60, mat)

    ans = [[0] * b for _ in range(b)]
    for i in range(b):
        ans[i][i] = 1
    for i in range(60):
        if (n >> i) & 1:
            ans = mat_product(ans, pow_lst[i])
    print(ans[0][0])


if __name__ == '__main__':
    MOD1 = 10**9 + 7
    main()
