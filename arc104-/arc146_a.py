from itertools import permutations


def main():
    ans = 0
    for l in permutations(A[-3:], 3):
        res = int(''.join(map(str, l)))
        ans = max(ans, res)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = sorted(map(int, input().split()))

    main()
