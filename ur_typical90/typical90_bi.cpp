#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll Q;
vecll T, X;

int main() {
    cin >> Q;
    T = vecll(Q), X = vecll(Q);
    rep(i, Q) cin >> T[i] >> X[i];

    vecll top(0), bottom(0);
    rep(i, Q) {
        ll t = T[i], x = X[i], ts = top.size();
        if (t == 1) top.push_back(x);
        if (t == 2) bottom.push_back(x);
        if (t == 3 && x <= ts) cout << top[ts - x] << '\n';
        if (t == 3 && x > ts) cout << bottom[x - ts - 1] << '\n';
    }
    return 0;
}
