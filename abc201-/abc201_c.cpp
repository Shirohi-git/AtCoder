#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define all(v) v.begin(), v.end()

ll smallcmb(ll n, ll r) {
    if (r < 0 || n < r) return 0;
    r = min(r, n - r);
    ll res = 1;
    rep(i, r) {
        res *= n - r + 1 + i;
        res /= i + 1;
    }
    return res;
}

string S;
vector<ll> CMB = {0, 1, 14, 36, 24};

int main() {
    cin >> S;
    ll o = count(all(S), 'o'), ox = count(all(S), '?');

    ll ans = 0;
    
    rep(i, ox + 1) {
        ll cnt = i + o;
        if (cnt == 0 || cnt > 4) continue;
        ans += CMB[cnt] * smallcmb(ox, i);
    }
    cout << ans << endl;
    return 0;
}
