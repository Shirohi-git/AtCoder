def main():
    def is_OK(div):
        if div < 2:
            return False
        num, cnt = N, 0
        while num:
            num, mod = divmod(num, div)
            cnt += mod
        return cnt == S
        
    for b in range(int(N**0.5)+1):
        if is_OK(b):
            return print(b)
    for i in range(int(N**0.5), 0, -1):
        b, m = divmod(N - S, i)
        if m == 0 and is_OK(b+1):
            return print(b+1)
    return print(N+1 if N == S else -1)

if __name__ == '__main__':
    N, S = int(input()), int(input())
    
    main()
