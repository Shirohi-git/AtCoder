#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, K;
const ll MOD1 = 1e9 + 7;

ll mod_pow(ll x, ll y, const ll& mod) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x) % mod;
        x = (x * x) % mod;
        y >>= 1;
    }
    return res;
}

int main() {
    cin >> N >> K;

    ll ans = K;
    if (N > 1) ans = ans * (K - 1) % MOD1;
    if (N > 2) ans *= mod_pow(K - 2, N - 2, MOD1);
    cout << ans % MOD1 << '\n';
    return 0;
}
