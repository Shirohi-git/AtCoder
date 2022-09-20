def main():
    incnt = [0] * N
    child = [[] for _ in range(N)]
    for a, b in AB:
        child[a - 1].append(b - 1)
        incnt[b - 1] += 1

    cnt = 0
    ans, lst = [[]], [[]]
    lst[0] = [i for i, num in enumerate(incnt) if num == 0]
    incnt = [incnt]

    def add_child(id, num):
        ans[id].append(num + 1)
        for i in child[num]:
            incnt[id][i] -= 1
            if incnt[id][i] == 0:
                lst[id].append(i)
        return

    def nxt_dfs(id_k, id_c, id_i, num):
        ans.append(ans[id_k][:])
        lst.append(lst[id_k][:])
        incnt.append(incnt[id_k][:])
        lst[id_c][id_i] = num
        return

    for k in range(K):
        if len(ans) < k+1:
            return print(-1)
        lst_k = lst[k]
        while lst_k:
            now = lst_k.pop()
            for i in range(len(lst_k)):
                cnt += 1
                if cnt >= K:
                    break
                nxt_dfs(k, cnt, i, now)
                add_child(cnt, lst_k[i])
            add_child(k, now)

    if any(len(ai) < N for ai in ans):
        return print(-1)
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
