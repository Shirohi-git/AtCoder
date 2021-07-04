def main():
    asort = sorted(A)
    adic = {asort[i]:i for i in range(N)}
    cnt = [K // N] * N
    for i in range(K % N):
        cnt[i] += 1
    
    for ai in A:
        print(cnt[adic[ai]])    
    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
