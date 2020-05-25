import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (n+1)
for i in a:
    cnt[i]+=1

for i in range(1, n+1):
    print(cnt[i])
