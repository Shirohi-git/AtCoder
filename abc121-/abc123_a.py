a, *_, e, k = (int(input()) for _ in range(6))

ans = (e - a > k)
print(':(' if ans else 'Yay!')
