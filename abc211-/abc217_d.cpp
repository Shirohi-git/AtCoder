#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll L, Q;
matll CX;

int main() {
    cin >> L >> Q;
    CX = matll(Q, vecll(2));
    rep(i, Q) cin >> CX[i][0] >> CX[i][1];

    set<ll> length = {0, L};
    repitr(cx, CX) {
        ll c = cx[0], x = cx[1];
        if (c == 1) length.insert(x);
        if (c == 2) {
            auto p = length.lower_bound(x);
            ll res = *p - *next(p, -1);
            cout << res << '\n';
        }
    }

    return 0;
}
