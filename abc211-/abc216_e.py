def main():
    from collections import Counter

    cnt, ans = 0, 0
    a_sort, a_cnt = sorted(set(A)), Counter(A)

    while cnt < K and len(a_sort) > 1:
        ai = a_sort.pop()
        ai_cnt = a_cnt[ai] * (ai - a_sort[-1])

        if (K - cnt) >= ai_cnt:
            cnt += ai_cnt
            ans += ai_cnt * (ai + a_sort[-1] + 1) // 2
            a_cnt[a_sort[-1]] += a_cnt[ai]
            a_cnt[ai] = 0
        else:
            div, mod = divmod(K - cnt, a_cnt[ai])
            cnt = K
            div_cnt = a_cnt[ai] * div
            ans += div_cnt * (2 * ai - div + 1) // 2
            ans += mod * (ai - div)

    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split())) + [0]

    main()
