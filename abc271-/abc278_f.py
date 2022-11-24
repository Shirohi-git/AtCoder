def main():
    near = [[0] * N for _ in range(N)]
    for i, si in enumerate(S):
        for j, sj in enumerate(S):
            if i != j and si[-1] == sj[0]:
                near[i][j] = 1

    res = [[0] * N for _ in range(1 << N)]
    for bit in range(1 << N)[::-1]:
        for i in range(N):
            for j in range(N):
                nxt = bit ^ (1 << j)
                if (bit >> i) & 1 and (bit >> j) & 1 == 0:
                    if near[i][j] == 1 and res[nxt][j] == 0:
                        res[bit][i] = 1

    ans = 'Second'
    for i in range(N):
        stt = res[1 << i][i]
        if stt == 0:
            ans = 'First'
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
