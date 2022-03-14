def main():

    def int_sqrt(num):
        res = int(num**0.5)-1
        while (res+1)**2 <= num:
            res += 1
        return res

    mx = max(X)
    dp, acc = [0, 1], [0, 1]
    for i in range(2, mx):
        if i ** 4 > mx:
            break
        dp.append(acc[int_sqrt(i)])
        acc.append(acc[-1] + dp[-1])

    for xi in X:
        root = int_sqrt(xi)
        ans = 0
        for i in range(1, int_sqrt(root)+1):
            ans += (root - i**2 + 1) * dp[i]
        print(ans)
    return


if __name__ == '__main__':
    T = int(input())
    X = [int(input()) for _ in range(T)]

    main()
