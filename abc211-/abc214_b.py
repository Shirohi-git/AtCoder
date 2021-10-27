def main():
    ans = 0
    for i in range(S+1):
        for j in range(S-i+1):
            for k in range(S-i-j+1):
                ans += (i*j*k <= T)
    return print(ans)


if __name__ == '__main__':
    S, T = map(int, input().split())

    main()
