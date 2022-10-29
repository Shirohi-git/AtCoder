from itertools import combinations


def main():
    def dist(p, q):
        (px, py, _), (qx, qy, _) = p, q
        return (px-qx)**2 + (py-qy)**2

    pos = [[i, j, S[i][j]] for i in range(9) for j in range(9)]
    ans = 0
    for a, b, c, d in combinations(pos, 4):
        if '.' in a + b + c + d:
            continue
        if dist(a, b) == dist(a, c) == dist(d, b) == dist(d, c):
            if dist(a, d) == dist(b, c):
                ans += 1
    return print(ans)


if __name__ == '__main__':
    S = [input() for _ in range(9)]

    main()
