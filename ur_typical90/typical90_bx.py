def main():
    sum_a = sum(A)
    if sum_a % 10:
        return print("No")

    a = A * 2
    l, now, cnt = 0, 0, sum_a // 10
    for ai in a:
        now += ai
        while now > cnt:
            now -= a[l]
            l += 1
        if now == cnt:
            return print("Yes")
    return print("No")


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    
    main()
