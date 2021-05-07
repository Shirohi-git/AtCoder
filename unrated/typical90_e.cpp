#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

const ll MOD1 = 1e9 + 7;

int main() {
    ll n, b, k;
    cin >> n >> b >> k;
    vector<ll> c(k);
    rep(i, k) cin >> c[i];

    vector<ll> pow10(61, 10 % b);
    rep(i, 60) pow10[i + 1] = (pow10[i] * pow10[i]) % b;

    matll dp(61, vector<ll>(b, 0));
    for_itr(ci, c) dp[0][ci % b] += 1;
    rep(p, 60) rep(i, b) rep(j, b) {
        ll nxt = (i * pow10[p] + j) % b;
        dp[p + 1][nxt] += dp[p][i] * dp[p][j];
        dp[p + 1][nxt] %= MOD1;
    }

    vector<ll> ans(b, 0), ZVEC(b, 0);
    ans[0] = 1;
    rep(p, 60) {
        if ((n >> p) & 1) {
            vector<ll> tmp = ZVEC;
            rep(i, b) rep(j, b) {
                ll nxt = (i * pow10[p] + j) % b;
                tmp[nxt] += ans[i] * dp[p][j];
                tmp[nxt] %= MOD1;
            }
            ans = tmp;
        }
    }
    cout << ans[0] << '\n';
    return 0;
}
