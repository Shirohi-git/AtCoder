def main():
    cnt = [[1]]
    for i in range(2, N+1):
        cnt.append(cnt[-1] + [i] + cnt[-1])
    return print(*cnt[-1])


if __name__ == '__main__':
    N = int(input())

    main()
