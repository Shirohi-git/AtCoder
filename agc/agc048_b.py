def main():
    def sub(x, y): return x-y
    evn = sorted(map(sub, A[::2], B[::2]))
    odd = sorted(map(sub, A[1::2], B[1::2]))

    sum_a = sum(A)
    ans, acc = sum_a, 0
    for ei, oi in zip(evn, odd):
        acc += ei + oi
        ans = max(ans, sum_a - acc)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
