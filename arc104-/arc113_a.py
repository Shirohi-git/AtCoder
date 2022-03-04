def main():
    ans = 0
    for a in range(1, K+1):
        bc = K // a
        for b in range(1, bc+1):
            ans += bc // b
    return print(ans)


if __name__ == '__main__':
    K = int(input())

    main()
