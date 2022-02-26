def main():
    cnt = 0
    flag = [0] * N
    loop = []
    for i in range(K):
        idx = cnt % N
        if flag[idx] >= 2:
            div, mod = divmod(K-i, len(loop))
            break
        elif flag[idx] >= 1:
            loop.append(A[idx])
        flag[idx] += 1
        cnt += A[idx]
    else:
        return print(cnt)
    cnt += sum(loop)*div + sum(loop[:mod])
    return print(cnt)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
