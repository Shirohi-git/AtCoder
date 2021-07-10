def main():
    def makedivisor(n0):
        p, upper, lower = 1, [], []
        while p * p <= n0:
            if n0 % p == 0:
                lower.append(p)
                if p * p != n0:
                    upper.append(n0 // p)
            p += 1
        return lower + upper[::-1]

    div_lst = makedivisor(K)
    ans = 0
    for di in div_lst:
        for dj in div_lst:
            if di > dj:
                continue
            div, mod = divmod(K, di * dj)
            if mod == 0:
                ans += (dj <= div)
    return print(ans)


if __name__ == '__main__':
    K = int(input())

    main()
