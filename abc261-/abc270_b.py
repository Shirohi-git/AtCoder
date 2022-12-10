def main():
    ans = abs(X)
    if 0 < Y < X or X < Y < 0:
        ans += [0, 2*abs(Z)][Y*Z < 0]
    if 0 < Y < Z < X or X < Z < Y < 0:
        ans = -1
    if 0 < Y < X < Z or Z < X < Y < 0:
        ans = -1
    return print(ans)


if __name__ == '__main__':
    X, Y, Z = map(int, input().split())

    main()
