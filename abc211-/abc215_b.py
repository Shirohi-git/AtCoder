def main():
    cnt, num = 0, 1
    while (num <= N):
        cnt += 1
        num *= 2
    return print(cnt-1)


if __name__ == '__main__':
    N = int(input())

    main()
