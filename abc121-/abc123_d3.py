def check(p, ans=0):
    cnt, lst = 0, []
    for ai in a:
        for bj in b:
            for ck in c:
                if ai + bj + ck < p:
                    break
                cnt += 1
                if ans:
                    lst.append(ai + bj + ck)
                if cnt >= k:
                    return True
    if ans:
        return sorted(lst)[::-1] + [ans] * (k - cnt)
    return False


def binary(l, r):
    while abs(r - l) > 1:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r


x, y, z, k = map(int, input().split())
a = sorted(map(int, input().split()))[::-1]
b = sorted(map(int, input().split()))[::-1]
c = sorted(map(int, input().split()))[::-1]

# 別解ver2 O(k**2 log Max)
point = binary(10 ** 11, -1)
print(*check(point + 1, point), sep='\n')
