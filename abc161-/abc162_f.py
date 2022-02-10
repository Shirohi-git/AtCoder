from itertools import accumulate


def main():
    def max_acc_dif(lst):
        dif = [ei-oi for ei, oi in lst]
        res = [0]
        for ai in accumulate(dif):
            res.append(max(res[-1], ai))
        return res
    
    frnt = max_acc_dif(zip(A[0::2], A[1::2]))[::-1]
    back = max_acc_dif([*zip(A[2::2], A[1::2])][::-1])

    ans = sum(A[1::2])
    if N % 2 == 0:
        ans += max(frnt)
    elif N % 2 == 1:
        dif_sum = [fi+bi for fi, bi in zip(frnt, back)]
        ans += max(dif_sum)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()