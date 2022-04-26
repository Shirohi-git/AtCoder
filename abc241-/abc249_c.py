from collections import Counter


def main():
    ans = 0
    cnt = [Counter(si) for si in S]
    for bit in range(2**N):
        now = Counter()
        for i in range(N):
            if (bit >> i) & 1:
                now += cnt[i]
        ans = max(ans, sum(ci == K for ci in now.values()))
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    main()
