from heapq import heapify, heappush, heappop

def main():
    
    def sumlst(ini, ad):
        res = [sum(ini)]
        heapify(ini)
        for ai in ad:
            res.append(res[-1])
            if ai > ini[0]:
                res[-1] += ai - heappop(ini)
                heappush(ini, ai)
        return res

    am = [-ai for ai in A]
    top = sumlst(A[:N], A[N:2*N])
    btm = sumlst(am[2*N:], am[N:2*N][::-1])
    
    ans = -(10**15)
    for ti, bi in zip(top, btm[::-1]):
        ans = max(ans, ti+bi)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()