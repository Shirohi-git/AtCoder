def main():

    def make_num(l0):
        res = []
        for i in range(1, 10):
            for j in range(-9, 9):
                if j == 0:
                    res.append(int(str(i) * l0))
                    continue
                lim = (10 if j > 0 else -1)
                num = ''.join(map(str, range(i, lim, j)))
                if len(num) >= l0:
                    res.append(int(num[:l0]))
        return res

    l,x = len(X), int(X)
    lst = make_num(l) + make_num(l+1)
    ans = min(li for li in lst if li >= x)
    return print(ans)


if __name__ == '__main__':
    X = input()

    main()
