def main():
    red, blue = [0] * N, [0] * N
    red[N-1] = 1
    for i in range(1, N)[::-1]:
        red[i-1] += red[i] + (blue[i] + red[i]*X)
        blue[i-1] += (blue[i] + red[i]*X) * Y
    return print(blue[0])


if __name__ == '__main__':
    N, X, Y = map(int, input().split())

    main()
