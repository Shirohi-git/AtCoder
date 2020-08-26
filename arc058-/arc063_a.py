s = input()

ans, stone = 0, s[0]
for i in s:
    if stone != i:
        ans += 1
        stone = i
print(ans)
