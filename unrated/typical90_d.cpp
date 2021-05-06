#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define max_itr(v) *max_element(v.begin(), v.end())
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define for_dic(key, val, dic) for (const auto& [key, val] : dic)

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w));
    rep(i, h) rep(j, w) cin >> a[i][j];

    vector<ll> sum_h(h, 0), sum_w(w, 0);
    rep(i, h) rep(j, w) sum_h[i] += a[i][j];
    rep(j, w) rep(i, h) sum_w[j] += a[i][j];

    rep(i, h) {
        rep(j, w) {
            ll tmp = sum_h[i] + sum_w[j] - a[i][j];
            cout << tmp << " ";
        }
        cout << "\n";
    }
    return 0;
}
