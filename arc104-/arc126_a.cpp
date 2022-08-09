#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll T;
matll Case;

int solve(ll a, ll b, ll c) {
    ll res = 0;

    ll res1 = min(b / 2, c);
    res += res1, b -= res1 * 2, c -= res1;

    ll res2 = min(a / 2, b / 2);
    res += res2, a -= res2 * 2, b -= res2 * 2;

    ll res3 = min(a, c / 2);
    res += res3, a -= res3, c -= res3 * 2;

    ll res4 = min(a / 3, c);
    res += res4, a -= res4 * 3, c -= res4;

    res += a / 5;
    cout << res << '\n';
    return 0;
}

int main() {
    cin >> T;
    Case = matll(T, vecll(3));
    rep(i, T) rep(j, 3) cin >> Case[i][j];

    rep(i, T) solve(Case[i][0], Case[i][1], Case[i][2]);
    return 0;
}
