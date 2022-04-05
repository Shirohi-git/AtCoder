def main():

    def choose(lst):
        if not lst:
            return [0]

        res = []
        x = lst.pop()
        for i in range(len(lst)):
            y = lst[i]
            if x > y:
                x, y = y, x
            a_xy = a[x][y]

            bfo = choose(lst[:i] + lst[i+1:])
            res += [a_xy ^ bi for bi in bfo]
        return res

    a = [[0] * (2*N-len(ai)) + ai for ai in A]
    ans = max(choose(list(range(2*N))[::-1]))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]

    main()
