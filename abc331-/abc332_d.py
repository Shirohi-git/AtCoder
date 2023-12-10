from itertools import permutations


def is_same(p, q):
    res = 1
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            res &= int(A[pi][qj] == B[i][j])
    return res


def calc(p, c):
    ans = 0
    for i in range(c):
        for j in range(i, c):
            if p[j] == i:
                p.insert(i, p.pop(j))
                ans += (j-i)
    return ans


def main():
    ans = INF
    for pi in map(list, permutations(range(H), H)):
        for qj in map(list, permutations(range(W), W)):
            if is_same(pi, qj):
                ans = min(calc(pi, H) + calc(qj, W), ans)
    return print(ans if ans < INF else -1)


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    INF = 10000

    main()
