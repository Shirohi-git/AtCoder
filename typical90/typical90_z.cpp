#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

int bfs(const int& s, const matll& near0, vecll& res) {
    res[s] = 0;
    deque<ll> que;
    que.push_back(s);
    while (!que.empty()) {
        ll q;
        q = que.front();
        que.pop_front();
        repitr(id, near0[q]) {
            if (res[id] > -1) continue;
            res[id] = res[q] ^ 1;
            que.push_back(id);
        }
    }
    return 0;
}

int main() {
    ll n;
    cin >> n;
    matll ab(n - 1, vector<ll>(2, -1));
    rep(i, n - 1) cin >> ab[i][0] >> ab[i][1];

    matll near(n, vector<ll>(0));
    repitr(id, ab) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }

    vecll dist(n, -1), odd(0), evn(0);
    bfs(0, near, dist);
    rep(i, n) {
        if (dist[i])
            odd.push_back(i);
        else
            evn.push_back(i);
    }

    vecll ans = odd;
    if (ll(2 * odd.size()) < n) ans = evn;
    rep(i, n / 2) cout << ans[i] + 1 << ' ';
    cout << endl;
    return 0;
}
