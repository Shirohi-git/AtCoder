h, w = map(int, input().split())

def Divisions(a, b):
    if a % 3 == 0:
        return 0
    else:
        cnt = b
        for i in range(a + 1):
            s = min(i * b, (a - i) * (b // 2))
            l = max(i * b, (a - i) * (b - b // 2))
            cnt = min(cnt, l - s)
        return cnt

print(min(Divisions(h, w), Divisions(w, h)))
