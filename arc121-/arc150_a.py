def main():
    for n, k, s in NKS:
        res, cnt_1 = 0, s.count('1')
        s = [*map(int, s.replace('?', '2'))]
        cnt = [*map(s[:k-1].count, range(3))]
        for i in range(k-1, n):
            cnt[s[i]] += 1
            if cnt[1] == cnt_1:
                res += (cnt[1] + cnt[2] == k)
            cnt[s[i-k+1]] -= 1
        print('Yes' if res == 1 else 'No')
    return


if __name__ == '__main__':
    T = int(input())
    NKS = [[*map(int, input().split()), input()] for _ in range(T)]

    main()
