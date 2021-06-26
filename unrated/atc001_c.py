def convolve(a, b):

    from math import pi as PI, cos, sin

    def FFT(lst, inv=False):
        n = len(lst)
        num = (n-1).bit_length()

        res = lst[:]
        for i in range(n):
            j = 0
            for k in range(num):
                j |= ((i >> k) & 1) << (num - 1 - k)
            if (i < j):
                res[i], res[j] = res[j], res[i]

        for i in range(num):
            i = (1 << i)
            for j in range(i):
                x = (2*inv - 1) * (2*PI*j) / (2*i)
                w = complex(cos(x), sin(x))
                for k in range(0, n, i*2):
                    s, t = res[j+k], res[i+j+k] * w
                    res[j+k], res[i+j+k] = s+t, s-t
        if (inv):
            res = [ri / n for ri in res]
        return res

    len_ab = len(a) + len(b) - 1
    n = 1 << len_ab.bit_length()

    a += [0] * (n-len(a))
    b += [0] * (n-len(b))

    res = [ai * bi for ai, bi in zip(FFT(a), FFT(b))]
    res = [int(fi.real + 0.1) for fi in FFT(res, True)[:len_ab]]
    return res


def main():
    a, b = [0], [0]
    for ai, bi in AB:
        a.append(ai), b.append(bi)
    ans = convolve(a, b)
    return print(*ans[1:], sep='\n')


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
