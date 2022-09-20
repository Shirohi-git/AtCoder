#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD1 = 1e9 + 7;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)

ll mod_pow(ll x, ll y, const ll& mod) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x) % mod;
        x = (x * x) % mod;
        y >>= 1;
    }
    return res;
}

class Combination {
   private:
    vector<ll> fact, inv, factinv;

   public:
    ll N, MOD;

    Combination(ll n0, ll mod) {
        N = n0, MOD = mod;
        fact = vector<ll>(N + 1, -1);
        inv = vector<ll>(N + 1, -1);
        factinv = vector<ll>(N + 1, -1);

        fact[0] = 1, fact[1] = 1;
        inv[0] = 0, inv[1] = 1;
        factinv[0] = 1, factinv[1] = 1;
        repi(i, 2, N + 1) {
            fact[i] = (fact[i - 1] * i) % MOD;
            inv[i] = mod_pow(i, MOD - 2, MOD);
            factinv[i] = (factinv[i - 1] * inv[i]) % MOD;
        }
    }

    ll count(ll cn, ll cr) {
        if ((cr < 0) || (cn < cr)) return 0;
        cr = min(cr, cn - cr);
        ll res = fact[cn] * factinv[cr] % MOD;
        res = res * factinv[cn - cr] % MOD;
        return (res % MOD + MOD) % MOD;
    }
};

int main() {
    ll n;
    cin >> n;

    Combination cmb(n, MOD1);
    repi(i, 1, n + 1) {
        ll ans = 0, sup = (n - 1) / i + 1;
        rep(j, sup) ans += cmb.count(n - i * j + j, j + 1);
        cout << ans % MOD1 << '\n';
    }
    return 0;
}
