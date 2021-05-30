#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n), b(n);
    rep(i, n) cin >> a[i];
    rep(i, n) cin >> b[i];
    sort_all(a), sort_all(b);

    ll ans = 0;
    rep(i, n) ans += abs(a[i] - b[i]);
    cout << ans << endl;
    return 0;
}
