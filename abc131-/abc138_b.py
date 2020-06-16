N = int(input())
a = list(map(int, input().split()))
for i in range(0, N):
    a[i] = 1/a[i]
print(1/sum(a))
