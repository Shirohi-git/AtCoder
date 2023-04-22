def main():
    ans = map(sum, AB)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()