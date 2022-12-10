def main():
    ans = len(T)
    for i, si, ti in zip(range(len(S)), S, T):
        if si != ti:
            ans = i+1
            break
    return print(ans)


if __name__ == '__main__':
    S, T = input(), input()

    main()
