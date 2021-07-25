def main():
    for i in range(2*H):
        print(C[i//2])
    return


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    main()
