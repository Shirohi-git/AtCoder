def main():
    cnt = [0] * (N+1)
    for ai in A:
        cnt[ai] += 1

    ans = 0
    for i in range((N+1)//2):
        al, ar = A[i], A[N-1-i]
        ans += (N - 2*i - cnt[al]) * (i+1)
        ans += (N - 2*i - cnt[ar]) * (i+1)
        if al != ar:
            ans -= i+1
        cnt[al] -= 1
        cnt[ar] -= 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
