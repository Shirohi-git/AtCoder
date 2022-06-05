def main():
    ans = 10000
    for i in NUM:
        time = set()
        for sj in S:
            idx = sj.index(i)
            while (idx in time):
                idx += 10
            time.add(idx)
        ans = min(ans, max(time))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    NUM = "0123456789"

    main()