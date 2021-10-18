def main():
    ans = [chr(pi-1 + ord('a')) for pi in P]
    return print(*ans, sep='')


if __name__ == '__main__':
    P = list(map(int, input().split()))

    main()
