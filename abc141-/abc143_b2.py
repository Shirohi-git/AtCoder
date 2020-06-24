n = int(input())
d = list(map(int, input().split()))

cnt, sumd = 0, sum(d) 
for i in d:
    cnt += i * (sumd - i)
print(cnt // 2)
