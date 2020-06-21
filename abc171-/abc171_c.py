n = int(input())

ans = ''
while n > 0:
    if n % 26 == 0:
        ans = chr(ord('a') + 25) + ans
        n = n // 26 - 1
    else:
        ans = chr(ord('a') + (n % 26) - 1) + ans
        n //= 26
print(ans)
