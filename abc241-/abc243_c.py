from collections import defaultdict


def main():
    rl = defaultdict(lambda: [MAX, MIN])
    for si, (xi, yi) in zip(S, XY):
        if si == 'R':
            rl[yi][0] = min(rl[yi][0], xi)
        if si == 'L':
            rl[yi][1] = max(rl[yi][1], xi)

    res = 0
    for r, l in rl.values():
        res |= (r < l)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    MIN, MAX = -1, 10**10

    main()
