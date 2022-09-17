#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))

ll N;
matll LR;

int main() {
    cin >> N;
    LR = matll(N, vecll(2));
    rep(i, N) cin >> LR[i][0] >> LR[i][1];

    ll l = 0, r = 10000000000;
    repitr(lri, LR) {
        ll res = 0;
        l = max(l, lri[0]), r = min(r, lri[1]);
        if (l > r) res = l - (l + r) / 2;
        cout << res << '\n';
    }

    return 0;
}
