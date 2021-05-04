#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < int(n); i++)
#define repi(i, a, b) for (int i = int(a); i < int(b); i++)

const ll MOD1 = pow(10, 9) + 7;

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    rep(i, n) { cin >> a[i]; }

    ll ans = 0, cnt = (k - 1) * k / 2 % MOD1;
    rep(i, n) {
        repi(j, i, n) {
            if (a[i] > a[j]) ans += k;
        }
        rep(j, n) {
            if (a[i] > a[j]) ans += cnt;
        }
        ans %= MOD1;
    }
    cout << ans << endl;
    return 0;
}
