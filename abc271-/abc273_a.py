def main():
    ans = 1
    for i in range(1, N+1):
        ans *= i
    return print(ans)


if __name__ == '__main__':
    N = int(input())

    main()
