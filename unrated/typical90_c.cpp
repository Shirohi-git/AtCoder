#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define max_itr(v) *max_element(v.begin(), v.end())
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

int nearlist(const vector<vector<ll>>& lst, vector<vector<ll>>& res) {
    for_itr(id, lst) {
        res[id[0] - 1].push_back(id[1] - 1);
        res[id[1] - 1].push_back(id[0] - 1);
    }
    return 0;
}

int bfs(const int& s, const vector<vector<ll>>& lst, vector<ll>& res) {
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

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> ab(n - 1, vector<ll>(2));
    rep(i, n - 1) { cin >> ab[i][0] >> ab[i][1]; }

    vector<vector<ll>> near(n, vector<ll>(0));
    nearlist(ab, near);

    vector<ll> dist(n, -1);
    bfs(0, near, dist);
    ll tmp = max_itr(dist), nxt = -1;
    rep(i, n) {
        if (tmp == dist[i]) nxt = i;
    }
    vector<ll> dist2(n, -1);
    bfs(nxt, near, dist2);
    ll ans = max_itr(dist2) + 1;
    cout << ans << endl;
    return 0;
}
