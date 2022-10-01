def main():
    def count_minus(num):  # num以下 は何個
        res, nxt = 0, 0
        for pi in l_pl:
            while nxt < len(l_mn) and pi * l_mn[nxt] <= num:
                nxt += 1
            res += nxt
        return res

    def count_zeros():
        mn, zr, pl = list(map(len, val))
        return zr*(mn+pl) + zr*(zr-1)//2

    def count_plus(num):  # num以下 は何個
        def count(lst):
            r, nxt = 0, 0
            for i, li in [*enumerate(lst)][::-1]:
                while nxt < len(lst) and li * lst[nxt] <= num:
                    nxt += 1
                r += min(nxt, i)
            return r

        res = count(l_pl) + count([-li for li in l_mn[::-1]])
        return res

    def binary(ng=-INF, ok=INF):
        def is_OK(num):  # c個以上 ある -> True
            cnt = count_minus(num)
            if num >= 0:
                cnt += count_zeros()
            if num > 0:
                cnt += count_plus(num)
            return (K <= cnt)

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    val = [[], [], []]
    for ai in A:
        val[(ai >= 0) + (ai > 0)].append(ai)
    l_mn, _, l_pl = list(map(sorted, val))
    ans = binary()
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    INF = max(-min(A), max(A))**2 + 1

    main()
