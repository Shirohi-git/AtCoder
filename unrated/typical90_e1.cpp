#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)

const ll MOD1 = 1e9 + 7;

// 小課題1 O(nb)
int main() {
    ll n, b, k;
    cin >> n >> b >> k;
    vector<ll> c(k);
    rep(i, k) { cin >> c[i]; }

    if (n > 1e4) return 0;
    matll dp(n + 1, vector<ll>(b, 0));
    for_itr(ck, c) dp[1][ck % b] += 1;
    repi(i, 1, n) rep(j, b) for_itr(ck, c) {
        ll nxt = (j * 10 + ck) % b;
        dp[i + 1][nxt] += dp[i][j];
        dp[i + 1][nxt] %= MOD1;
    }
    cout << dp[n][0] << '\n';
    return 0;
}
