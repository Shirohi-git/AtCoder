n = int(input())
s = [''.join(sorted(input())) for i in range(n)]
ans = 0
dict = {}
for i in s:
    if i in dict:
        ans += dict[i]
        dict[i] += 1
    else:
        dict[i] = 1
print(ans)
