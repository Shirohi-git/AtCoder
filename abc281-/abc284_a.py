def main():
    return print(*S[::-1], sep='\n')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()