n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    cnt ^= i
for i in a:
    print(cnt ^ i)
