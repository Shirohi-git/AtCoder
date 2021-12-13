def d(r):
 s=[0]
 while s:
  q=s.pop();f[q]=0
  for p in e[q]:
   if f[p]:s+=p,;r+=p+1,;break
 return r[::-1]
N,_,*A=map(int,open(0).read().split())
f=[1]*N;e=[[]for _ in f];A=iter(A)
for a,b in zip(A,A):e[a-1]+=b-1,;e[b-1]+=a-1,
z=d(d([1]));print(len(z),*z)