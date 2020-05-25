m, d = map(int, input().split())
cnt = 0
for i in range(1, m+1):
    for j in range(1, d+1):
        d_10 = j//10
        d_1 = j % 10
        if (d_1 >= 2) & (d_10 >= 2):
            if i == d_10*d_1:
                cnt += 1
print(cnt)
