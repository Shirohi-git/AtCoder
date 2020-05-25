s = str(input())
r_s = s[::-1]
cnt = 0

for i in range(len(s) // 2):
    if s[i] != r_s[i]:
        cnt += 1

print(cnt)
