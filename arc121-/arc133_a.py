def main():
    bfo = 0
    for ai in A + [0]:
        if ai < bfo:
            res = bfo
            break
        bfo = ai
    ans = [ai for ai in A if ai != res]
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
