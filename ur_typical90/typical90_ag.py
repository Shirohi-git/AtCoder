def main():
    ans = ((H+1) // 2) * ((W+1) // 2)
    return print(ans if min(H, W) > 1 else H * W)

if __name__ == '__main__':
    H, W = map(int, input().split())
    main()
