def main():
    ans = []
    for a, s in AS:
        xo = s - 2*a
        res = (xo >= 0 and (a & xo) == 0)
        ans.append("Yes" if res else "No")
    return print(*ans, sep='\n')


if __name__ == '__main__':
    T = int(input())
    AS = [list(map(int, input().split())) for _ in range(T)]

    main()