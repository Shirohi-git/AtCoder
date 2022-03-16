#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll H, W;
const ll MOD9 = 998244353;
vecs S;

ll mod_pow(ll x, ll y, const ll& mod) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x) % mod;
        x = (x * x) % mod;
        y >>= 1;
    }
    return res;
}

bool is_ingrid(ll x, ll y) {
    if (x < 0 || H <= x) return false;
    if (y < 0 || W <= y) return false;
    return true;
}

int main() {
    cin >> H >> W;
    S = vecs(H);
    rep(i, H) cin >> S[i];

    ll cnt = 0;
    rep(k, H + W - 1) {
        char now = '.';
        rep(i, k + 1) {
            ll j = k - i;
            if (!is_ingrid(i, j)) continue;
            if (now == '.') now = S[i][j];
            if (S[i][j] != '.' && now != S[i][j]) {
                cout << 0 << '\n';
                return 0;
            }
        }
        if (now == '.') cnt += 1;
    }
    ll ans = mod_pow(2, cnt, MOD9);
    cout << ans << '\n';
    return 0;
}
