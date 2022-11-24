def main():
    cnt = len(set(aij for ai in A for aij in ai))
    a_rng = [[H+1, -1, W+1, -1] for _ in range(N+1)]
    for i, ai in enumerate(A):
        for j, aij in enumerate(ai):
            a_rng[aij][0] = min(a_rng[aij][0], i)
            a_rng[aij][1] = max(a_rng[aij][1], i)
            a_rng[aij][2] = min(a_rng[aij][2], j)
            a_rng[aij][3] = max(a_rng[aij][3], j)

    for i in range(H-P+1):
        ans = []
        for j in range(W-Q+1):
            p, q = i+P, j+Q
            res = cnt
            for mn_x, mx_x, mn_y, mx_y in a_rng[1:]:
                if i <= mn_x <= mx_x < p and j <= mn_y <= mx_y < q:
                    res -= 1
            ans.append(res)
        print(*ans)
    return


if __name__ == '__main__':
    H, W, N, P, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    main()
