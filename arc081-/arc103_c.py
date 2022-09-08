def main():
    if S[0] ^ 1 or S[-1]:
        return print(-1)
    if any(S[i] ^ S[N-2-i] for i in range(N-1)):
        return print(-1)

    ans = []
    bfo, nxt = 0, 1
    for size in [i+1 for i in range(1, N//2) if S[i]]:
        ans.append((bfo, nxt))
        ans += [(nxt, nj) for nj in range(nxt+1, size)]
        bfo, nxt = nxt, size
    ans.append((bfo, nxt))
    ans += [(nxt, ni) for ni in range(nxt+1, N)]

    for ai, bi in ans:
        print(ai+1, bi+1)
    return


if __name__ == '__main__':
    S = [*map(int, input())]
    N = len(S)

    main()
