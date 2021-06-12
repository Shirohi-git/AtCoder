from itertools import accumulate


def main():
    ans = 10**10
    sum_a = sum(A)
    acc = list(accumulate(A))
    for i, x in enumerate(A):
        tmp = x * (i+1) + sum_a - acc[i]
        tmp = (sum_a - tmp) / N + x / 2
        ans = min(ans, tmp)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = sorted(map(int, input().split()))[::-1]

    main()
