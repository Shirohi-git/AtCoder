s = list(input())
t = list(input())
cnt = 0
for i in range(3):
    if t[i] == s[i]:
        cnt += 1
print(cnt)
