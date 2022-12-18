def output():
    res = []
    for i in range(K):
        w = (1 << i) - 1
        res += [(j, j+w) for j in range(1, N+1-w)]
    print(len(res))
    for ri in res:
        print(*ri)
    return {lr: i for i, lr in enumerate(res, 1)}


def main():
    for _ in range(Q):
        l, r = map(int, input().split())
        k = max(i for i in range(K) if (1 << i) <= r - l + 1)
        w = (1 << k) - 1
        a, b = D[l, l+w], D[r-w,r]
        print(a, b)
    return


if __name__ == '__main__':
    N = int(input())
    K = 12
    D = output()

    Q = int(input())
    main()
