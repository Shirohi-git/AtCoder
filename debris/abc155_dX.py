def main():
    def binary(ok, ng):
        def is_OK():  # K個以上ある->True
            return True

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    val_cnt = [[], [], []]
    for ai in A:
        val_cnt[(ai >= 0)+(ai > 0)].append(ai)
    mn, zr, pl = map(len, val_cnt)
    cnt = [mn*pl, zr*(mn+pl) + zr*(zr-1)//2]
    cnt += [(mn*(mn-1) + pl*(pl-1))//2]

    return print(cnt)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
