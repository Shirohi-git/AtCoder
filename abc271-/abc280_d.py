from collections import Counter


def main():
    def factorize(n0):
        p, res = 2, []
        while p * p <= n0:
            while n0 % p == 0:
                n0 //= p
                res.append(p)
            p += 1
        if n0 > 1:
            res.append(n0)
        return res

    prime = Counter(factorize(K))
    ans = 0
    for pi, ci in prime.items():
        cnt, num = ci, 0
        while cnt > 0:
            num += pi
            num2 = num
            while num2 % pi == 0:
                cnt -= 1
                num2 //= pi
        ans = max(ans, num)
    return print(ans)


if __name__ == '__main__':
    K = int(input())

    main()
