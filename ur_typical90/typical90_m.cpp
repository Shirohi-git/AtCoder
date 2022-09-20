#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

const ll INF = 1LL << 40;

int dijkstra(const int& s, const vector<matll>& w_near, vector<ll>& dist) {
    dist[s] = 0;
    priority_queue<vector<ll>> que;
    que.push({0, s});
    while (que.size() > 0) {
        ll d = que.top()[0], q = que.top()[1];
        que.pop();
        if (dist[q] < -d) continue;
        for_itr(nq, w_near[q]) {
            ll nxt = nq[0], tmp = -d + nq[1];
            if (dist[nxt] > tmp) {
                dist[nxt] = tmp;
                que.push({-tmp, nxt});
            }
        }
    }
    return 0;
}

int main() {
    ll n, m;
    cin >> n >> m;
    matll abc(m, vector<ll>(3));
    rep(i, m) rep(j, 3) cin >> abc[i][j];

    vector<matll> near(n, matll(0));
    vector<ll> dist_1(n, INF), dist_N(n, INF);
    for_itr(id, abc) {
        near[id[0] - 1].push_back({id[1] - 1, id[2]});
        near[id[1] - 1].push_back({id[0] - 1, id[2]});
    }
    dijkstra(0, near, dist_1), dijkstra(n - 1, near, dist_N);
    rep(i, n) cout << dist_1[i] + dist_N[i] << '\n';
    return 0;
}
