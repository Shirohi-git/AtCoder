def main():
    
    def is_ok_idx(s, t):
        res = []
        flag = set()
        t_idx = 0
        for si in s:
            while (si not in flag):
                if t_idx >= N:
                    t_idx = N+1
                    break
                flag.add(t[t_idx])
                t_idx += 1
            res.append(t_idx-1)
        return res

    a_inb, b_ina = is_ok_idx(A, B), is_ok_idx(B, A)
    for x, y in XY:
        x, y = x-1, y-1
        ans = (a_inb[x] <= y and b_ina[y] <= x)
        print("Yes" if ans else "No")
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    XY = [list(map(int, input().split())) for _ in range(Q)]
    
    main()