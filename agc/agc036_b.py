from bisect import bisect_right


def main():
    def loopout(idx):
        div, mod = divmod(N*K, idx)
        res = loop[bisect_right(loop, mod)-1]
        return idx*div + res

    def next_id(idx):
        ai_id = a_id[A[idx % N]]
        res = ai_id[bisect_right(ai_id, idx % N)]
        res += idx - idx % N + 1
        return res

    a_id = [[] for _ in range(max(A)+1)]
    for i, ai in enumerate(A*2):
        a_id[ai].append(i)

    loop, flag = [], set()
    now, nxt = -1, 0
    while nxt < N*K:
        now, nxt = nxt, next_id(nxt)
        if now % N in flag:
            now = loopout(now)
            break
        loop.append(now), flag.add(now % N)

    ans = []
    while now < N*K:
        nxt = next_id(now)
        if nxt <= N*K:
            now = nxt
        else:
            ans.append(A[now % N])
            now += 1
    return print(*ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
