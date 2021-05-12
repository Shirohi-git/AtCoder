#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define all(v) v.begin(), v.end()
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n + 2, 1LL << 31);
    a[0] = -(1LL << 31);
    rep(i, n) cin >> a[i + 1];
    sort_all(a);

    ll q;
    cin >> q;
    vector<ll> b(q);
    rep(i, q) cin >> b[i];

    for_itr(bi, b) {
        auto pos = lower_bound(all(a), bi);
        cout << min(bi - *(pos - 1), *pos - bi) << '\n';
    }
    return 0;
}
