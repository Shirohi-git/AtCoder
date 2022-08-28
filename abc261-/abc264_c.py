from itertools import combinations as cmb


def main():
    res = 0
    for col in cmb(range(H1), H2):
        for row in cmb(range(W1), W2):
            a = []
            for c in col:
                a.append([A[c][r] for r in row])
            if a == B:
                res = 1
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    main()
