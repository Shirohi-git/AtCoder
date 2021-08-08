def main():
    a = sorted(set(ai for ai, _ in AB))
    a_dic = {a[i]: i+1 for i in range(len(a))}
    b = sorted(set(bi for _, bi in AB))
    b_dic = {b[i]: i+1 for i in range(len(b))}

    for ai, bi in AB:
        print(a_dic[ai], b_dic[bi])
    return


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
