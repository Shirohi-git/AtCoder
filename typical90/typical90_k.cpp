#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define max_itr(v) *max_element(v.begin(), v.end())
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

int main() {
    ll n;
    cin >> n;
    matll dcs(n, vector<ll>(3, 0));
    rep(i, n) rep(j, 3) cin >> dcs[i][j];

    sort_all(dcs);
    vector<ll> dp(10000, 0);
    for_itr(vec, dcs) {
        ll d = vec[0], c = vec[1], s = vec[2];
        rep(tmp, d - c + 1) {
            ll i = (d - c) - tmp;
            dp[i + c] = max(dp[i + c], dp[i] + s);
        }
    }
    cout << max_itr(dp) << endl;
    return 0;
}
