def main():
    def binary(c, p, ng=-INF, ok=INF):
        mn, pl = val_cnt[::2]

        if p == 1:
            return 0

        def count_minus(num):  # num以下 は何個
            res, nxt = 0, 0
            for pi in pl:
                while nxt < len(mn) and pi * mn[nxt] <= num:
                    nxt += 1
                res += nxt
            return res

        def count_plus(num):  # num以下 は何個
            res = 0
            m_nxt = len(mn) - 1
            for i, mi in [*zip(range(len(mn))[::-1], mn)]:
                while m_nxt >= 0 and mi * mn[m_nxt] <= num:
                    m_nxt -= 1
                res += min(len(mn) - m_nxt - 1, i)
            p_nxt = 0
            for i, pi in [*enumerate(pl)][::-1]:
                while p_nxt < len(pl) and pi * pl[p_nxt] <= num:
                    p_nxt += 1
                res += min(p_nxt, i)
            return res

        def is_OK(num):  # c個以上 ある -> True
            if p == 0:
                cnt = count_minus(num)
            if p == 2:
                cnt = count_plus(num)
            return (c <= cnt)

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    val_cnt = [[], [], []]
    for ai in A:
        val_cnt[(ai >= 0) + (ai > 0)].append(ai)
    val_cnt = list(map(sorted, val_cnt))
    mn, zr, pl = list(map(len, val_cnt))
    cnt = [mn*pl, zr*(mn+pl) + zr*(zr-1)//2]
    cnt += [mn*(mn-1)//2 + pl*(pl-1)//2]

    k, ptn = K, -1
    for i in range(3):
        if k <= cnt[i]:
            ptn = i
            break
        k -= cnt[i]

    ans = binary(k, ptn)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    INF = max(-min(A), max(A))**2 + 1

    main()
