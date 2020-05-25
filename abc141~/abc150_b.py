n = int(input())
s = list(str(input()))
ans=0
for i in range(len(s) - 2):
    if s[i] == 'A':
        if s[i + 1] == 'B':
            if s[i + 2] == 'C':
                ans+=1
print(ans)