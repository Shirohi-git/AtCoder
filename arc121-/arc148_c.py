def main():
    child_cnt = [0] * N
    for pi in P[1:]:
        child_cnt[pi-1] += 1

    for vi in V:
        res = 0
        set_vi = set(vi)
        for vij in vi:
            res += 1 + child_cnt[vij-1]
            if P[vij-1] in set_vi:
                res -= 2
        print(res)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    P = [-1] + list(map(int, input().split()))
    V = [list(map(int, input().split()))[1:] for _ in range(Q)]

    main()
