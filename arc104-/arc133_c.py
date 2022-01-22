def main():

    def max_mod(num, inf):
        r = inf // K * K + num
        r -= K * (r > inf)
        return r

    res = (sum(A) % K == sum(B) % K)
    amax, bmax = K*W-W, K*H-H
    ans1 = sum(max_mod(ai, amax) for ai in A)
    ans2 = sum(max_mod(bi, bmax) for bi in B)

    return print(min(ans1, ans2) if res else -1)


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
