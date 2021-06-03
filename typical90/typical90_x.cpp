#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n), b(n);
    rep(i, n) cin >> a[i];
    rep(i, n) cin >> b[i];

    string ans = "Yes";
    rep(i, n) k -= abs(a[i] - b[i]);
    if (k < 0 || k % 2) ans = "No";
    cout << ans << endl;
    return 0;
}
