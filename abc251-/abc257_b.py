def main():
    koma = sorted(A) + [N+1]
    idx = sorted(range(K), key=lambda x: A[x])
    for li in L:
        koma[li-1] += (koma[li] != koma[li-1]+1)
    ans = [-1] * K
    for id, ki in zip(idx, koma):
        ans[id] = ki
    return print(*ans)


if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    main()
