#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < int(n); i++)

ll n;
vector<ll> a(pow(10, 6));
const ll MOD9 = 998244353;

int main() {
    cin >> n;
    rep(i, n) { cin >> a[i]; }
    sort(a.begin(), a.begin() + n);

    ll ans = 0, big = 0;
    for (int i = n - 1; i >= 0; i--) {
        big = (big + a[i]) % MOD9;
        ans = (ans + a[i] * big) % MOD9;
        ans = (ans + MOD9) % MOD9;
        big = 2 * big - a[i];
    }
    cout << ans << endl;
}
