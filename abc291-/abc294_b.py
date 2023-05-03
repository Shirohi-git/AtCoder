def main():
    for ai in A:
        ans = [chr(ORD_A+aij-1) if aij > 0 else '.' for aij in ai]
        print(*ans, sep='')
    return


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ORD_A = ord('A')

    main()
