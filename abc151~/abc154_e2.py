n = int(input())
k = int(input())


def k1(n):
    str1_n = str(n)
    keta1 = len(str1_n)
    cnt = 9 * (keta1 - 1) + int(str1_n[0])
    return cnt


def k2(n):
    str2_n = str(n)
    keta2 = len(str2_n)
    cnt = 81 * (keta2 - 1) * (keta2 - 2) // 2
    cnt += (int(str2_n[0]) - 1) * k1(10 ** (keta2 - 1) - 1)
    cnt += k1(n - (int(str2_n[0]) * 10 ** (keta2 - 1)))
    return cnt


def k3(n):
    str3_n = str(n)
    keta3 = len(str3_n)
    t = 0
    for i in range(keta3-2):
        t += (i+1)*i//2
    cnt = 729 * t
    cnt += (int(str3_n[0]) - 1) * k2(10 ** (keta3 - 1) - 1)
    cnt += k2(n - (int(str3_n[0]) * 10 ** (keta3 - 1)))
    return cnt


if k == 1:
    ans = k1(n)

if k == 2:
    ans = k2(n)

if k == 3:
    ans = k3(n)

print(ans)
