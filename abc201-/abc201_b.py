def main():
    ts = sorted((int(ti), si) for si, ti in ST)
    return print(ts[-2][1])


if __name__ == '__main__':
    N = int(input())
    ST = [input().split() for _ in range(N)]

    main()
