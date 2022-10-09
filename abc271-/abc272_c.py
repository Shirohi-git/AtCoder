def main():
    odd = sorted(ai for ai in A if ai % 2 == 1)
    evn = sorted(ai for ai in A if ai % 2 == 0)
    ans  = -1
    if len(odd) >= 2:
        ans = max(sum(odd[-2:]), ans)
    if len(evn) >= 2:
        ans = max(sum(evn[-2:]), ans)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
