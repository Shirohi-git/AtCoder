def main():
    ans = []
    cnt = 0
    for si in S:
        if cnt >= K:
            si = 'x'
        elif si == 'o':
            cnt += 1
        ans.append(si)
    return print(*ans, sep='')


if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()

    main()
