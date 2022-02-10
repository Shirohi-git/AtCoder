def main():
    for j in range(W):
        print(*[ai[j] for ai in A])
    return


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    main()
