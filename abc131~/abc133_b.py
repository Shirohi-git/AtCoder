import numpy

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
cnt=0
for i in range(n-1):
    for j in range(i + 1, n):
        a = numpy.array(x[i])
        b = numpy.array(x[j])
        num=numpy.linalg.norm(a-b)
        if num.is_integer() == True:
            cnt += 1
print(cnt)