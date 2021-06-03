from collections import Counter


def main():
    cnt = Counter(A)
    lst = [(0, -1)]
    for i in range(N):
        if lst[-1][0] < A[i]:
            lst.append((A[i], i))

    ans = [0] * N
    nxt, now = lst[-1]
    for num in sorted(cnt)[::-1]:
        if num == nxt:
            nxt, now = lst[-2][0], lst[-1][1]
            lst.pop()
        ans[now] += cnt[num] * (num - nxt)
        cnt[nxt] += cnt[num]
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
