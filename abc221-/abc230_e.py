def main():
    ans, now, div = 0, N, 1
    while now - N//(div+1) > 1:
        ans += now
        div += 1
        now = N // div
    while now >= 1:
        cnt = N//now - N//(now+1)
        ans += now * cnt
        now -= 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())

    main()
