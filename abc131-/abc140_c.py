n = int(input())
b = list(map(int, input().split()))
a = b[0]
for i in range(1,n-1):
    a += min(b[i], b[i - 1])
a += b[-1]
print(a)
