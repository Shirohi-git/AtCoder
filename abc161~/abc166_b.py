n, k = map(int, input().split())
A = [None]*k
for i in range(k):
    d = int(input())
    A[i] = list(map(int, input().split()))

snuke = [0] * n
for i in range(k):
    for j in A[i]:
        snuke[j - 1] += 1

ans = 0
for i in snuke:
    if i == 0:
        ans += 1
print(ans)