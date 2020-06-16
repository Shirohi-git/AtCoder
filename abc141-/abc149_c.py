import math
import sys

x = int(input())

for i in range(x, 100004):
    ans = True
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            ans = False
            break
    if ans == True:
        print(i)
        sys.exit()
