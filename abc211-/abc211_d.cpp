#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, M;
matll AB;
const ll MOD1 = 1e9 + 7;

ll bfs(const ll& s0, const ll& n0, const matll& near0) {
    vecll res(n0, -1), cnt(n0, 0);
    res[s0] = 0, cnt[s0] = 1;
    deque<ll> que;
    que.push_back(s0);

    while (!que.empty()) {
        ll q = que.front();
        que.pop_front();
        repitr(id, near0[q]) {
            if (res[id] == res[q] + 1) cnt[id] = (cnt[id] + cnt[q]) % MOD1;
            if (res[id] > -1) continue;
            res[id] = res[q] + 1;
            cnt[id] = cnt[q];
            que.push_back(id);
        }
    }
    return cnt[n0 - 1];
}

int main() {
    cin >> N >> M;
    AB = matll(M, vecll(2, 0));
    rep(i, M) cin >> AB[i][0] >> AB[i][1];

    matll near(N, vecll(0));
    repitr(id, AB) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }
    cout << bfs(0, N, near) << endl;

    return 0;
}
