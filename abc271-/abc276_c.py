def main():
    idx = N
    for i in range(N)[::-1]:
        if all(p < q for p, q in zip(P[i:], P[i+1:])):
            idx = i

    nxt = max(pi for pi in P[idx:] if pi < P[idx-1])
    ans = P[:idx-1] + [nxt]
    ans += sorted(pi for pi in P[idx-1:] if pi != nxt)[::-1]
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    main()
