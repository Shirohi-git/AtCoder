n = map(int, list(input()))

ans = 0
for i in n:
    ans = (ans + i) % 9
print('Yes' if ans % 9 == 0 else 'No')
