def main():

    def weight(X, Y):
        res = set()
        for xi in range(0, F+1, X):
            for yi in range(0, F+1-xi, Y):
                res.add(xi + yi)
        return sorted(res)

    w, s = weight(100*A, 100*B), weight(C, D)
    ans = (max(w), 0)
    for wi in w:
        for si in s:
            if (100 * si > E * wi) or (si + wi > F):
                break
            if ans[1] * wi <= si * ans[0]:
                ans = (wi, si)
    return print(sum(ans), ans[1])


if __name__ == '__main__':
    A, B, C, D, E, F = map(int, input().split())

    main()
