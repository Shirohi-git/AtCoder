#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)

const ll INF = pow(10LL, 15);

int main() {
    ll n, n2;
    cin >> n, n2 = 2 * n;
    vector<ll> a(n2, 0);
    rep(i, n2) cin >> a[i];

    matll dp(n2, vector<ll>(n2 + 1, INF));
    reprs(j, 0, n2 + 1, 2) rep(l, n2) {
        ll r = l + j;
        if (l == r)
            dp[l][r] = 0;
        else if (r <= n2) {
            dp[l][r] = min(dp[l][r], dp[l + 1][r - 1] + abs(a[l] - a[r - 1]));
            reprs(k, l, r, 2) dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r]);
        }
    }
    cout << dp[0][n2] << endl;
    return 0;
}
