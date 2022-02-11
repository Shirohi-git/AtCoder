def main():
    ab = sorted(AB, key=lambda x: -x[0])
    ans, wei = 0, W
    for ai, bi in ab:
        ans += min(wei, bi) * ai
        wei -= min(wei, bi)
    return print(ans)


if __name__ == '__main__':
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
