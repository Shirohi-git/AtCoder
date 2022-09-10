from itertools import permutations


def main():
    cnt = INF - (sum(len(si) for si in S) + N-1)
    for prm in permutations(S):
        prm = [*prm]
        dp = [prm[0]]
        for pi in prm[1:]:
            nxt = []
            for dj in dp:
                for num in range(cnt+1):
                    res = dj + '_'*(num+1) + pi
                    if len(res) > INF:
                        break
                    nxt.append(res)
            dp = nxt

        for dj in dp:
            if dj not in T and len(dj) >= 3:
                return print(dj)
    return print(-1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = set(input() for _ in range(M))
    INF = 16

    main()
