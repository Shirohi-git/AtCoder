#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n;
    cin >> n;
    vector<ll> abc(3);
    rep(i, 3) cin >> abc[i];
    sort_all(abc);

    ll ans = 1e5;
    rep(i, n / abc[2] + 1) rep(j, (n - abc[2] * i) / abc[1] + 1) {
        ll tmp = n - abc[2] * i - abc[1] * j;
        if (tmp % abc[0] == 0) ans = min(ans, i + j + tmp / abc[0]);
    }
    cout << ans << endl;
    return 0;
}
