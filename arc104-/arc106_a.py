n = int(input())

pow3 = [pow(3, i + 1) for i in range(39)]
pow5 = [pow(5, i + 1) for i in range(29)]

for i in range(39):
    for j in range(29):
        if pow3[i] + pow5[j] == n:
            print(i + 1, j + 1)
            exit()
print(-1)
