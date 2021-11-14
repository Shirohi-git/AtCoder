def main():
    return print(len(LA))


if __name__ == '__main__':
    N = int(input())
    LA = set(tuple(map(int, input().split()[1:])) for _ in range(N))

    main()
