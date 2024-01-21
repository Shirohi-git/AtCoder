def main():
    ans = -1
    for i in range(101):
        a = sorted(A + [i])
        if sum(a[1:-1]) >= X:
            ans = i
            break
    return print(ans)


if __name__ == '__main__':
    N, X = [*map(int, input().split())]
    A = [*map(int, input().split())]
    main()
