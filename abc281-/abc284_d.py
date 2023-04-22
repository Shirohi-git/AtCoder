def main():
    def factorize(n0):
        r = 2
        while r * r <= n0:
            if n0 % r == 0:
                return r
            r += 1
        return r
    
    p, q = factorize(N), -1
    if N % p**2 == 0:
        q = N // p**2
    else:
        p, q = round((N // p)**0.5), p
    return print(p, q)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())

        main()
