from collections import defaultdict


def main():
    near = defaultdict(set)
    for t, a, b in TAB:
        if t == 1:
            near[a].add(b)
        elif t == 2:
            if b in near[a]:
                near[a].remove(b)
        else:  # elif t == 3:
            res = (b in near[a] and a in near[b])
            print('Yes' if res else 'No')
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    TAB = [list(map(int, input().split())) for _ in range(Q)]

    main()
