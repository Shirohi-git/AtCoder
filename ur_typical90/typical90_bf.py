def main():
    num = N
    flag = [-1] * MOD
    for i in range(K):
        if flag[num] > -1:
            loop = i-flag[num]
            idx = flag[num] + (K-i) % loop
            num = flag.index(idx)
            break
        flag[num] = i
        num += sum(map(int, str(num)))
        num %= MOD
    return print(num)


if __name__ == '__main__':
    N, K = map(int, input().split())
    MOD = 10**5

    main()
