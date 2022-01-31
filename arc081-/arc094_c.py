def main():
    sum_a = last = sum(ai for ai, bi in AB)
    if any(ai != bi for ai, bi in AB):
        last = min(bi for ai, bi in AB if ai > bi)
    ans = sum_a - last
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    AB = list(list(map(int, input().split())) for _ in range(N))

    main()