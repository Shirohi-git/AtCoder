#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define max_val(v) *max_element(v.begin(), v.end())
#define max_idx(v) distance(v.begin(), max_element(v.begin(), v.end()))
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

int bfs(const int& s, const matll& lst, const int& dis_or_id) {
    vector<ll> res(lst.size(), -1);
    res[s] = 0;
    deque<ll> que;
    que.push_back(s);

    while (!que.empty()) {
        ll q = que.front();
        que.pop_front();
        for_itr(id, lst[q]) {
            if (res[id] > -1) continue;
            res[id] = res[q] + 1;
            que.push_back(id);
        }
    }
    if (dis_or_id == 1) return max_idx(res);
    return max_val(res);
}

int main() {
    ll n;
    cin >> n;
    matll ab(n - 1, vector<ll>(2));
    rep(i, n - 1) cin >> ab[i][0] >> ab[i][1];

    matll near(n, vector<ll>(0));
    for_itr(id, ab) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }

    ll nxt = bfs(0, near, 1);
    ll ans = bfs(nxt, near, 0) + 1;
    cout << ans << endl;
    return 0;
}
