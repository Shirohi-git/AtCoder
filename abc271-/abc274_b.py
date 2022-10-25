def main():
    ans = []
    for i in range(W):
        res = 0
        for j in range(H):
            res += (C[j][i] == '#')
        ans.append(res)
    return print(*ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    main()
