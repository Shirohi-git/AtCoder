s = input()

stone = [s[0]]
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        stone.append(s[i])
print(len(stone) - 1)
