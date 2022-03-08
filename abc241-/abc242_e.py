def count(n, x):
    res = 1
    for i, xi in enumerate(x):
        res += pow(26, n-i-1, MOD9) * (ord(xi)-Ord_A)
        res %= MOD9
    return res


def main():
    for n, s in NS:
        t = s[:(n+1)//2]
        mx = t
        if t + t[-1 - (n & 1)::-1] > s:
            mx, bfo = [], 1
            for ti in t[::-1]:
                if bfo and ti == 'A':
                    mx.append('Z')
                else:
                    mx.append(chr(ord(ti) - bfo))
                    bfo -= bfo
            mx = ''.join(mx[::-1])
        print(count(len(mx), mx))
    return


if __name__ == '__main__':
    T = int(input())
    NS = [[int(input()), input()] for _ in range(T)]
    MOD9 = 998244353
    Ord_A = ord('A')

    main()
