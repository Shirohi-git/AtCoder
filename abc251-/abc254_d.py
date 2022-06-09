from bisect import bisect_right


def main():
    sqar = [i**2 for i in range(1, 500)]
    ans = 0
    for i in range(1, N+1):
        num = i
        for s in sqar[1:]:
            if num < s:
                break
            while num % s == 0:
                num //= s
        ans += bisect_right(sqar, N//num)
    return print(ans)


if __name__ == '__main__':
    N = int(input())

    main()
