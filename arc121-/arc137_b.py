def main():
    acc, a_mx, a_mn = 0, 0, 0
    mx, mn = 0, 0
    for ai in A:
        acc += (-ai*2) + 1
        a_mx, a_mn = max(a_mx, acc), min(a_mn, acc)
        mx, mn = max(mx, acc-a_mn), min(mn, acc-a_mx)
    ans = (mx - mn +1)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    
    main()
