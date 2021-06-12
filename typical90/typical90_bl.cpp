#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define sum(v) accumulate(v.begin(), v.end(), 0LL)

ll N, Q;
vecll A;
matll LRV;

int main() {
    cin >> N >> Q;
    A = vecll(N), LRV = matll(Q, vecll(3));
    rep(i, N) cin >> A[i];
    rep(i, Q) rep(j, 3) cin >> LRV[i][j];

    vecll cost(N - 1);
    rep(i, N - 1) cost[i] = A[i] - A[i + 1];
    ll ans = 0;
    repitr(ci, cost) ans += abs(ci);
    repitr(id, LRV) {
        ll l = id[0], r = id[1], v = id[2];
        if (0 <= l - 2) {
            ans += abs(cost[l - 2] - v) - abs(cost[l - 2]);
            cost[l - 2] -= v;
        }
        if (r - 1 < N - 1) {
            ans += abs(cost[r - 1] + v) - abs(cost[r - 1]);
            cost[r - 1] += v;
        }
        cout << ans << '\n';
    }
    return 0;
}
