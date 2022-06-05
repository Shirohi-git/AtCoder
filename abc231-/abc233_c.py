from itertools import product


def main():
    ans = 0
    for pdt in product(*A):
        cnt = 1
        for pi in pdt:
            cnt *= pi
        ans += (cnt == X)
    return print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]

    main()