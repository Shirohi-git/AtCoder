def main():
    wht, blk = '.'*B, '#'*B
    ans_w = ''.join((blk if i % 2 else wht) for i in range(N))
    ans_b = ''.join((wht if i % 2 else blk) for i in range(N))
    for i in range(A*N):
        print(ans_b if i//A % 2 else ans_w)
    return


if __name__ == '__main__':
    N, A, B = map(int, input().split())

    main()
