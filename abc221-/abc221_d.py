def main():
    from collections import Counter

    imos = Counter()
    for a, b in AB:
        imos[a] += 1
        imos[a+b] -= 1
    day = sorted(imos.keys())

    ans = [0] * (N+1)
    for bfo, now in zip(day, day[1:]):
        imos[now] += imos[bfo]
        ans[imos[bfo]] += now - bfo
    return print(*ans[1:])


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
