def main():
    a = sorted(set(A))
    cnt = {}
    for i, ai in enumerate(a):
        cnt[ai] = len(a)-1 - i

    ans = [0] * N
    for ai in A:
        ans[cnt[ai]] += 1
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
