def main():
    t = T
    for i, ai in enumerate(A):
        if  XY and XY[-1][0] == i+1:
            t += XY.pop()[1]
        t -= ai
        if t <= 0:
            return print("No")
    return print("Yes")


if __name__ == '__main__':
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)][::-1]

    main()
