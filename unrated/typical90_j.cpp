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

    vector<ll> acc1(n + 1, 0), acc2(n + 1, 0);
    rep(i, n) {
        ll c = cp[i][0], p = cp[i][1];
        acc1[i + 1] = acc1[i];
        acc2[i + 1] = acc2[i];
        if (c == 1)
            acc1[i + 1] += p;
        else if (c == 2)
            acc2[i + 1] += p;
    }
    rep(i, q) {
        ll l = lr[i][0], r = lr[i][1];
        ll ans1 = acc1[r] - acc1[l - 1];
        ll ans2 = acc2[r] - acc2[l - 1];
        cout << ans1 << ' ' << ans2 << '\n';
    }
    return 0;
}
