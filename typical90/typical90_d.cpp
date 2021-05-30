#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w));
    vector<ll> sum_h(h, 0), sum_w(w, 0);
    rep(i, h) rep(j, w) {
        cin >> a[i][j];
        sum_h[i] += a[i][j];
        sum_w[j] += a[i][j];
    }

    rep(i, h) rep(j, w) {
        ll tmp = sum_h[i] + sum_w[j] - a[i][j];
        cout << tmp << " ";
    }
    cout << "\n";
    return 0;
}
