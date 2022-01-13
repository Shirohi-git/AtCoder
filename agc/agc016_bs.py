N,*A=map(int,open(0).read().split())
x,n=max(A),min(A)
print("NYoe s"[1-(x+1<N<2*x)&(x==n)|(2*x-N<=A.count(n)<n+1==x)::2])