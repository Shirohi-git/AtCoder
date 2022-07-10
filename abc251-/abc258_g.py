def popcount(num):
    res = (num & 0x5555555555555555) + ((num >> 1) & 0x5555555555555555)
    res = (res & 0x3333333333333333) + ((res >> 2) & 0x3333333333333333)
    res = (res & 0x0f0f0f0f0f0f0f0f) + ((res >> 4) & 0x0f0f0f0f0f0f0f0f)
    res = (res & 0x00ff00ff00ff00ff) + ((res >> 8) & 0x00ff00ff00ff00ff)
    res = (res & 0x0000ffff0000ffff) + ((res >> 16) & 0x0000ffff0000ffff)
    res = (res & 0x00000000ffffffff) + ((res >> 32) & 0x00000000ffffffff)
    return res


def main():
    a = []
    for Ai in A:
        a += [[int(Ai[k:k+B], 2) for k in range(0, N, B)]]

    ans = 0
    for i in range(N):
        for j in range(i):
            if A[i][j] == '0':
                continue
            for aik, ajk in zip(a[i], a[j]):
                ans += popcount(aik & ajk)
    return print(ans // 3)


if __name__ == '__main__':
    N = int(input())
    A = [input() for _ in range(N)]
    B = 63

    main()
