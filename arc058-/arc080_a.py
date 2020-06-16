n = int(input())
a = list(map(int, input().split()))
cnt4,cnt2=0,0
for i in a:
    if i % 4 == 0:
        cnt4 += 1
    elif i % 2 == 0:
        cnt2 += 1

cnt2 = max(1,cnt2)
print('Yes' if 2 * cnt4 + cnt2 >= n else 'No')