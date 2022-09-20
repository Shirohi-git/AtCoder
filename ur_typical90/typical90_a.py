def binary(left, right):
    while abs(right - left) > 1:
        mid = (left + right) // 2
        cnt, bfo = 0, 0
        for ai in a:
            if ai - bfo >= mid and l - ai >= mid:
                cnt += 1
                bfo = ai
        if cnt >= k:
            right = mid
        else:
            left = mid
    return right


n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

ans = binary(l+1, -1)
print(ans)
