from itertools import accumulate


def main():
    def shakutori(s, t, lim):
        res = acc[t] - acc[s]
        while t+1 <= N and res+A[t+1] <= lim:
            t, res = t+1, res+A[t+1]
        return res, t

    acc = [*accumulate(A)]
    y, z, w = 0, 0, 0
    for x in range(N):
        p, y = shakutori(x, y, P)
        q, z = shakutori(y, z, Q)
        r, w = shakutori(z, w, R)
        if (p, q, r) == (P, Q, R):
            return print("Yes")
    return print("No")


if __name__ == '__main__':
    N, P, Q, R = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    main()
