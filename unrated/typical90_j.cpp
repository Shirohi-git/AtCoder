#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n;
    cin >> n;
    matll cp(n, vector<ll>(2, 0));
    rep(i, n) cin >> cp[i][0] >> cp[i][1];
    ll q;
    cin >> q;
    matll lr(q, vector<ll>(2, 0));
    rep(i, q) cin >> lr[i][0] >> lr[i][1];

    matll acc(2, vector<ll>(n + 1, 0));
    rep(i, n) {
        ll c = cp[i][0], p = cp[i][1];
        rep(j, 2) acc[j][i + 1] = acc[j][i];
        acc[c - 1][i + 1] += p;
    }
    rep(i, q) {
        ll l = lr[i][0], r = lr[i][1];
        vector<ll> ans(2, 0);
        rep(j, 2) ans[j] = acc[j][r] - acc[j][l - 1];
        cout << ans[0] << ' ' << ans[1] << '\n';
    }
    return 0;
}
