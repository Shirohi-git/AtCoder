def main():
    point = []
    for a, b in AB:
        point += [b, a-b]
    ans = sum(sorted(point)[-K:])
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
