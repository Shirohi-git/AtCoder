y, m, d = map(int, input().split('/'))

ans = 'Heisei'
if ((y > 2019) or (y == 2019 and m > 4)
        or (y == 2019 and m == 4 and d > 30)):
    ans = 'TBD'
print(ans)
