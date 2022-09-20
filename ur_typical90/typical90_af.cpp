#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n, m;
    cin >> n;
    matll a(n, vecll(n, 0));
    rep(i, n) rep(j, n) cin >> a[i][j];
    cin >> m;
    matll bad(n, vecll(n, 0));
    rep(i, m) {
        ll x, y;
        cin >> x >> y;
        bad[x - 1][y - 1]++, bad[y - 1][x - 1]++;
    }

    ll ans = 10001;
    vecll perm(n);
    rep(i, n) perm[i] = i;

    do {
        ll time = 0;
        rep(i, n) time += a[perm[i]][i];
        rep(i, n - 1) if (bad[perm[i]][perm[i + 1]]) time = 10001;
        ans = min(ans, time);
    } while (next_permutation(perm.begin(), perm.end()));

    if (ans >= 10001) ans = -1;
    cout << ans << endl;
    return 0;
}
