def main():
    ans = 4
    ans -= ([1, H].count(R)) + ([1, W].count(C))
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    main()
