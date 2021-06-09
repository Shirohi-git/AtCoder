from itertools import permutations


def main():
    bad = [[0] * N for _ in range(N)]
    for x, y in XY:
        bad[x - 1][y - 1] = 1
        bad[y - 1][x - 1] = 1

    ans = 10001
    for lst in permutations(list(range(N))):
        lst = list(lst)
        if any(bad[lst[i]][lst[i+1]] for i in range(N-1)):
            continue
        time = sum(A[li][i] for i, li in enumerate(lst))
        ans = min(ans,time)
    return print(ans if ans < 10001 else -1)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    XY = [list(map(int, input().split())) for _ in range(M)]

    main()
