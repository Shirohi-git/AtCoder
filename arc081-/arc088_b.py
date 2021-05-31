def main():
    n = len(S)
    s = S + '2'
    acc = [0] + [i+1 for i in range(n) if s[i] != s[i+1]]
    ans = max(min(n - acc[i-1], acc[i]) for i in range(1, len(acc)))
    return print(ans)


if __name__ == '__main__':
    S = input()
    main()
