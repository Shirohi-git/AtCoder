import collections as z
N,S,a,c=int(input()),input(),[0],z.Counter()
def q(s,r):
 p=lambda g:''.join(s[i]for i in range(N)if b>>i&1==g)
 for b in range(1<<N):d,e=p(0),p(1)[::-1];c[d,e]+=r;a[0]-=~-r*c[e,d]
q(S[:N],1);q(S[N:],0);print(*a)