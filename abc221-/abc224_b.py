def main():
    ans = 1
    for i in range(H**2):
        i1, i2 = divmod(i, H)
        if i1 >= i2:
            continue
        a1, a2 = A[i1], A[i2]
        for j in range(W**2):
            j1, j2 = divmod(j, W)
            if j1 < j2:
                ans &= (a1[j1]+a2[j2] <= a1[j2]+a2[j1])
    return print("Yes" if ans else "No")


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    main()