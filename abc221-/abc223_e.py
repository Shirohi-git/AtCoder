def ceil(a, b):
    return (a + b - 1) // b


def put_sq(x, y, sizes):
    if x <= 0 or y <= 0:
        return False
    if len(sizes) == 1:
        sx = ceil(sizes[0], y)
        return (sx <= x)
    
    res = False
    lst1, lst2 = [], sizes[:]
    while lst2:
        s = lst2.pop()
        nxt = lst1 + lst2
        res |= put_sq(x, y - ceil(s, x), nxt)
        res |= put_sq(x - ceil(s, y), y, nxt)
        lst1.append(s)
    return res


def main():
    ans = put_sq(X, Y, ABC)
    return print("Yes" if ans else "No")


if __name__ == '__main__':
    X, Y, *ABC = map(int, input().split())

    main()