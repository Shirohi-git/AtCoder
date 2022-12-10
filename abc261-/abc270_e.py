def main():
    def binary(ok, ng):
        def is_OK(num):
            cnt = sum(min(ai, num) for ai in A)
            return cnt <= K
    
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    m = binary(-1, K+1)
    k = K - sum(min(ai, m) for ai in A)
    ans = [max(0, ai-m) for ai in A]
    for i in range(N):
        if k > 0 and ans[i] > 0:
            ans[i] -= 1
            k -= 1
    return print(*ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
