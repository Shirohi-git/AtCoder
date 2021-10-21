from collections import Counter


def main():
    ans = N**2
    ans -= sum(ai**2 for ai in A.values())
    return print(ans // 2)


if __name__ == '__main__':
    N = int(input())
    A = Counter(map(int, input().split()))

    main()
