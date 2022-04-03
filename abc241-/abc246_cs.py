N,K,X,*A=map(int,open(0).read().split())
for i in range(N):c=min(K,A[i]//X);A[i]-=c*X;K-=c
print(sum(sorted(A)[:N-K]))