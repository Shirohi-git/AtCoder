#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

ld solve(ll t, ll l, ll x, ll y, ll now) {
    ld theta = 2 * M_PI * (now % t) / ld(t), l2 = ld(l) / 2;
    ld px = 0, py = -l2 * cos(theta - M_PI_2);
    ld pz = l2 * sin(theta - M_PI_2) + l2;
    ld dist = pow(pow(x - px, 2) + pow(y - py, 2), 0.5);
    return rad_to_deg(atan2(pz, dist));
}

int main() {
    ll t, l, x, y, q;
    cin >> t >> l >> x >> y >> q;
    vector<ll> e(q);
    rep(i, q) cin >> e[i];

    for_itr(ei, e) {
        ld ans = solve(t, l, x, y, ei);
        coutdeci << ans << '\n';
    }
    return 0;
}
