def main():
    ans = int(N**0.5)
    while ans * (ans+1) // 2 < N:
        ans += 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())

    main()
