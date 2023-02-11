def main():
    ans = 0
    for bit in range(1 << M):
        num = 0
        for i in range(M):
            if not bit >> i & 1:
                continue
            for aij in CA[i]:
                num |= 1 << (aij-1)
        ans += (num == (1 << N) - 1)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    CA = []
    for _ in range(M):
        _ = input()
        CA.append(list(map(int, input().split())))

    main()
