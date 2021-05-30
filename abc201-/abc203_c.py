def main():
    ans = K
    for a, b in sorted(AB):
        if a > ans:
            break
        ans += b
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
