#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define max_val(v) *max_element(v.begin(), v.end())

ll N;
vecll W, B;

int main() {
    cin >> N;
    W = vecll(N), B = vecll(N);
    rep(i, N) cin >> W[i];
    rep(i, N) cin >> B[i];

    ll max_w = max_val(W);
    ll lim = (max_w + 1) * max_w / 2 + max_val(B) + 1;
    matll gd(max_w + 1, vecll(lim, -1));
    rep(i, max_w + 1) rep(j, lim) {
        vecll mex(lim, 1);
        if (i > 0 and j + i < lim) mex[gd[i - 1][j + i]] = 0;
        repr(k, 1, j / 2 + 1) mex[gd[i][j - k]] = 0;
        rep(num, lim) if (mex[num]) {
            gd[i][j] = num;
            break;
        }
    }

    ll res = 0;
    rep(i, N) res ^= gd[W[i]][B[i]];
    string ans = "First";
    if (!res) ans = "Second";
    cout << ans << endl;
    return 0;
}
