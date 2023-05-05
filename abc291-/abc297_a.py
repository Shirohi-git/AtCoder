def main():
    ans = -1
    for t1, t2 in zip(T, T[1:]):
        if t2-t1 <= D:
            return print(t2)
    return print(ans)


if __name__ == '__main__':
    N, D = map(int, input().split())
    T = list(map(int, input().split()))

    main()
