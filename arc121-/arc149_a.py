def main():
    res = []
    for num in range(1, 10):
        cnt, mod = 1, num % M
        while cnt <= N:
            if mod == 0:
                cnt = N // cnt * cnt
                break
            cnt += 1
            mod = (mod*10 + num) % M
        else:
            cnt, num = -1, -1
        res.append((cnt, num))
    cnt, ans = sorted(res)[-1]
    return print(str(ans) * cnt if cnt != -1 else -1)


if __name__ == '__main__':
    N, M = map(int, input().split())

    main()
