class str_acc:

    def __init__(self, w):
        self.acc = [0]
        for wi in w:
            nxt = (wi == 'A') - (wi == 'B')
            self.acc.append(self.acc[-1] + nxt)

    def query(self, l, r):
        return (self.acc[r] - self.acc[l-1]) % 3


def main():
    sacc, tacc = str_acc(S), str_acc(T)
    for a, b, c, d in ABCD:
        ans = (sacc.query(a, b) == tacc.query(c, d))
        print("YES" if ans else "NO")


if __name__ == '__main__':
    S, T = input(), input()
    Q = int(input())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]

    main()
