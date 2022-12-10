def main():
    ans = sum(si.count('#') for si in S)
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    main()
