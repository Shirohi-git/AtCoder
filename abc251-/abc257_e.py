def main():
    min_c = min(C)
    ans_len = N // min_c

    cost = N
    ans = []
    for i in range(ans_len):
        for j in range(M)[::-1]:
            if cost - C[j] >= min_c * (ans_len-i-1):
                ans.append(j+1)
                cost -= C[j]
                break
    return print(*ans, sep='')


if __name__ == '__main__':
    N, M = int(input()), 9
    C = list(map(int, input().split()))

    main()
