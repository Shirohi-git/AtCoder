def main():
    pnt = dict()
    for i in range(N)[::-1]:
        si, ti = ST[i]
        pnt[si] = (int(ti), i)

    mx = max(pnt.values())[0]
    ans = N+1
    for si, (ti, idx) in pnt.items():
        if ti == mx:
            ans = min(ans, idx+1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    ST = [input().split() for _ in range(N)]

    main()
