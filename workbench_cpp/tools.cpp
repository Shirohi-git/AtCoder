#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define max_itr(v) *max_element(v.begin(), v.end())
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define for_dic(key, val, dic) for (const auto& [key, val] : dic)

//隣接リスト
int nearlist(const matll& lst, matll& res) {
    for_itr(id, lst) {
        res[id[0] - 1].push_back(id[1] - 1);
        res[id[1] - 1].push_back(id[0] - 1);
    }
    return 0;
}

//幅優先探索
int bfs(const int& s, const matll& lst, vector<ll>& res) {
    res[s] = 0;
    deque<ll> que;
    que.push_back(s);

    while (!que.empty()) {
        ll q;
        q = que.front();
        que.pop_front();
        for_itr(id, lst[q]) {
            if (res[id] > 0) continue;
            res[id] = res[q] + 1;
            que.push_back(id);
        }
    }
    return 0;
}

//二分探索判定
bool isOK(ll mid) {
    bool res;
    if (res)
        return true;
    else
        return false;
}

//二分探索
int binary_search(ll l, ll r) {
    int left = l, right = r + 1;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (isOK(mid) == false)
            right = mid;
        else
            left = mid;
    }
    return left;
}

//行列積
int mat_product(matll a, matll b, matll& res) {
    ll n = a.size(), m = b.size(), l = b[0].size();
    if (m != a[0].size()) {
        cout << "can't\n";
        return 0;
    }
    rep(i, n) rep(j, l) rep(k, m) { res[i][j] += a[i][k] * b[k][j]; }
    return 0;
}

//行列累乗 res[i] = mat**(2**i)
int mat_powlst(ll cnt, matll mat, vector<matll>& res) {
    res[0] = mat;
    rep(p, cnt) mat_product(res[p], res[p], res[p + 1]);
    return 0;
}
