from collections import Counter

n = int(input())
k = len(str(n))
cnt = Counter(map(lambda x: int(x) % 3, str(n)))

if n % 3 == 0:
    print(0)
elif n % 3 == 1:
    if cnt[1] >= 1 and k > 1:
        print(1)
    elif cnt[2] >= 2 and k > 2:
        print(2)
    else:
        print(-1)
elif n % 3 == 2:
    if cnt[2] >= 1 and k > 1:
        print(1)
    elif cnt[1] >= 2 and k > 2:
        print(2)
    else:
        print(-1)
