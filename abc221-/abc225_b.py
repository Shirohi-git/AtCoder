def main():
    
    for u in AB[0]:
        if all((u in ab) for ab in AB):
            return print('Yes')
    return print('No')


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    main()
