def main():
    cnt = [1]
    bfo = S[0]
    for si in S[1:]:
        cnt[-1] += (si == bfo)
        if si != bfo:
            cnt.append(1)
        bfo = si
    ans = (N+1) * N // 2
    ans -= sum((ci+1) * ci // 2 for ci in cnt)
    return print(ans)


if __name__ == '__main__':
    N, S = int(input()), input()

    main()
