#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto &id : itr)

ll N, M;
matll AB, NEAR;

ll bfs(const int &s0, const ll &n0, const matll &near0) {
    ll cnt = 1;
    vecll res(n0, -1);
    res[s0] = 0;
    deque<ll> que;
    que.push_back(s0);

    while (!que.empty()) {
        ll q;
        q = que.front();
        que.pop_front();
        repitr(id, near0[q]) {
            if (res[id] > -1) continue;
            res[id] = res[q] + 1;
            cnt++;
            que.push_back(id);
        }
    }
    return cnt;
}

int main() {
    cin >> N >> M;
    AB = matll(M, vecll(2));
    rep(i, M) rep(j, 2) cin >> AB[i][j];

    NEAR = matll(N, vecll(0));
    repitr(id, AB) NEAR[id[0] - 1].push_back(id[1] - 1);
    ll ans = 0;
    rep(i, N) ans += bfs(i, N, NEAR);
    cout << ans << endl;
    return 0;
}
