# A05
N, K = map(int, input().split())
ans = sum(0 < K-a-b-2 <= N for a in range(N) for b in range(N))
print(ans)

# A04
N = bin(int(input()))[2:]
print(N.zfill(10))

# A03
N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
res = any(pi+qi == K for pi in P for qi in Q)
print('Yes' if res else 'No')

# A02
_, X = map(int, input().split())
A = set(map(int, input().split()))
print('Yes' if X in A else 'No')

# A01
print(int(input())**2)
