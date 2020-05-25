n=int(input())
p=list(map(int,input().split()))
max_p=p[0]
cnt=0
for i in range(n):
    if p[i]!= i+1:
        cnt+=1
if cnt>2:
    print('NO')
else :
    print('YES')
