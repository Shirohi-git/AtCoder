from itertools import product


def main():
    def move_knight(x, y):
        res = []
        for (a, b), (p, q) in product(MINUS, MOVE):
            nx, ny = x + a*p, y + b*q
            res.append((nx, ny))
        return set(res)

    x_set = move_knight(SX, SY)
    y_set = move_knight(TX, TY)
    ans = bool(x_set & y_set)
    return print('Yes' if ans else 'No')


if __name__ == '__main__':
    SX, SY, TX, TY = map(int, input().split())
    MOVE = [(1, 2), (2, 1)]
    MINUS = [*product([1, -1], repeat=2)]

    main()
