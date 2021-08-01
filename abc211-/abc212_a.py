def main():
    ans = ['', "Gold", "Silver", "Alloy"]
    idx = (A > 0) + (B > 0) * 2
    return print(ans[idx])


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
