from itertools import accumulate


def main():
    cnt = [0] * (max(A)+1)
    for ai in A:
        cnt[ai] += 1
    acc = list(accumulate(cnt))
    
    ans = 0
    for ai in A:
        ans += acc[ai-1] * (acc[-1] - acc[ai])
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    
    main()