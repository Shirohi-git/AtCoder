def main():
    max_w = max(W)
    lim = (max_w+1) * max_w // 2 + max(B)+1
    gd = [[-1] * lim for _ in range(max_w+1)]
    for i in range(max_w+1):
        for j in range(lim):
            mex = [1] * lim
            if (i > 0 and j+i < lim):
                mex[gd[i-1][j+i]] = 0
            for k in range(1, j//2 + 1):
                    mex[gd[i][j-k]] = 0
            for num in range(lim):
                if (mex[num]):
                    gd[i][j] = num
                    break

    res = 0
    for wi, bi in zip(W, B):
        res ^= gd[wi][bi]
    return print("First" if res else "Second")


if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
