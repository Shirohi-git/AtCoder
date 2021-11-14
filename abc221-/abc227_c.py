def main():
    ans = 0
    for a in range(1, N+1):
        if a**3 > N:
            break
        for b in range(a, N+1):
            if a*b*b > N:
                break
            ans += (N//(a*b)) - b + 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    main()
