def solve(LIST):
    n, *times, d = LIST
    cnt, stack = {n: 0, 0: n * d}, [n]

    while stack:
        q = stack.pop()
        if q <= 1:
            continue
        lst = []
        for num, cost in zip([2, 3, 5], times):
            mod, nxt = q % num, q // num
            lst.append((mod, nxt, cost))
            mod, nxt = (num - mod) % num, (q + num - 1) // num
            lst.append((mod, nxt, cost))

        cnt[0] = min(cnt[0], q * d + cnt[q])
        for mod, nxt, cost in lst:
            nxt_cost = mod * d + cost + cnt[q]
            if (nxt not in cnt) or (nxt_cost < cnt[nxt]):
                cnt[nxt] = nxt_cost
                stack.append(nxt)
    return min(cnt[1] + d, cnt[0])


t = int(input())
nabcd = [map(int, input().split()) for _ in range(t)]

for test in nabcd:
    print(solve(test))
