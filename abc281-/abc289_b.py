def main():
    ans, tmp = [], []
    for i in range(1,N+1):
        if i == P[-1]:
            tmp.append(P.pop())
        else:
            ans.append(i)
            ans += tmp[::-1]
            tmp = []
    return print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    P = [0] + list(map(int, input().split()))[::-1]

    main()
