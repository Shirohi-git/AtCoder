def add_num(mod):
    for li in lst[n-1:]:
        if li % 6 == mod:
            return li


n = int(input())

if n <= 10:
    ans = [2, 3, 25] + [30 * (i+1) for i in range(7)]
    exit(print(*ans[:n]))

lst = [i for i in range(2, 30001) if (i % 2) * (i % 3) == 0]
mod6 = sum(lst[:n-1]) % 6

lst[n-1] = add_num([0, -1, 4, 3, -1, 4][mod6])
lst[5] += (add_num(0) - 9) * (mod6 == 5)
print(*lst[:n])
