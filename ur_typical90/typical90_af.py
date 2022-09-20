from itertools import permutations


def main():
    bad = [[0] * N for _ in range(N)]
    for x, y in XY:
        bad[x - 1][y - 1] = 1
        bad[y - 1][x - 1] = 1

    ans = 10001
    for lst in permutations(range(N)):
        time = 0
        for i, li in enumerate(lst):
            if i > 0 and bad[lst[i-1]][li]:
                break
            time += A[li][i]
        else:
            ans = min(ans, time)
    return print(ans if ans < 10001 else -1)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    XY = [list(map(int, input().split())) for _ in range(M)]

    main()
