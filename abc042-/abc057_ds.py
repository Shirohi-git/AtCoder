import math
n,a,b,*v=map(int,open(0).read().split());v.sort();d=v.count(e:=v[-a-1]);c=d-v[:-a].count(e)
print(f:=sum(v[-a:])/a,sum(math.comb(d,i)for i in range(c,min(c+(b-a)*(f==e),d)+1)))