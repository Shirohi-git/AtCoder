from collections import defaultdict


def main():

    def pmax(e2, e1):
        return (INF if e2 == e1 else e1)

    pcnt = defaultdict(lambda: [0, 0])
    for pe in PE:
        for p, e in pe:
            pcnt[p] = sorted(pcnt[p] + [e])[-2:]

    ans = set()
    for pe in PE:
        res = tuple(p for p, e in pe if pmax(*pcnt[p]) == e)
        ans.add(res)
    return print(len(ans))


if __name__ == '__main__':
    N = int(input())
    PE = []
    for _ in range(N):
        m = int(input())
        PE.append([list(map(int, input().split())) for _ in range(m)])
    INF = 10**9 + 1

    main()
