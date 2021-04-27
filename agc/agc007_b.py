n = int(input())
p = list(map(int, input().split()))

a = [n * (i+1) for i in range(n)]
b = a[::-1]
for i, pi in enumerate(p):
    b[pi-1] += i
print(*a), print(*b)
