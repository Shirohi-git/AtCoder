N,X,Y,*A=map(int,open(0).read().split())
z=0;x=y=l=-1
for i,a in enumerate(A):
 if a==X:x=i
 if a==Y:y=i
 if X<a or a<Y:l=i
 z+=max(0,min(x,y)-l)
print(z)