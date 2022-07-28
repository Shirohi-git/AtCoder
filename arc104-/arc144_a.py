def main():
    div, mod = divmod(N, 4)
    m = div*8 + mod*2
    res = [str(mod)]*(mod > 0)+ ['4']*div
    ans = ''.join(res)
    return print(m, ans, sep='\n')


if __name__ == '__main__':
    N = int(input())

    main()