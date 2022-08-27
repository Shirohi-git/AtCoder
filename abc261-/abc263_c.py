from itertools import combinations


def main():
    for num in combinations(range(1, M+1), N):
        print(*num)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())

    main()
