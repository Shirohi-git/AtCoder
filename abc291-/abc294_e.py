def main():
    v, u = -1, -1
    v_cnt = u_cnt = 0
    ans = 0
    for v, lv in VL:
        if v == u:
            ans += min(lv, u_cnt - v_cnt)
        v_cnt += lv
        if u_cnt >= v_cnt:
            continue

        for u, lu in UL:
            if u == v:
                ans += min(lu, v_cnt - u_cnt)
            u_cnt += lu
            if u_cnt >= v_cnt:
                break
    return print(ans)


if __name__ == '__main__':
    L, N, M = map(int, input().split())
    VL = [list(map(int, input().split())) for _ in range(N)]
    UL = iter([list(map(int, input().split())) for _ in range(M)])

    main()
