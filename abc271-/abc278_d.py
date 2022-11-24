def main():
    def reset(idx, cnt):
        if reset_flg[idx] != cnt:
            reset_flg[idx] = cnt
            a[idx] = 0
        return

    a = [0] + A[:]
    reset_flg = [0] * (N+1)
    reset_cnt, base = 0, 0
    for que in Query:
        if que[0] == 1:
            reset_cnt += 1
            base = que[1]
        else:
            reset(que[1], reset_cnt)
            if que[0] == 2:
                a[que[1]] += que[2]
            else:  # elif que[0] == 3:
                print(a[que[1]] + base)
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
