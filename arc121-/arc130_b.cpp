#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))
#define all(v) (v).begin(), (v).end()

template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id << ' ';
    cout << '\n';
    return;
}

ll H, W, C, Q;
matll TNC;

int main() {
    cin >> H >> W >> C >> Q;
    TNC = matll(Q, vecll(3, 0));
    rep(i, Q) rep(j, 3) cin >> TNC[i][j];

    ll h = H, w = W;
    vecll ans(C, 0);
    set<ll> hflg, wflg;
    reverse(all(TNC));

    repitr(tnc, TNC) {
        ll t = tnc[0], n = tnc[1] - 1, c = tnc[2] - 1;
        if (t == 1 && hflg.find(n) == hflg.end()) {
            h--, ans[c] += w, hflg.insert(n);
        } else if (t == 2 && wflg.find(n) == wflg.end()) {
            w--, ans[c] += h, wflg.insert(n);
        }
    }
    coutitr(ans);
    return 0;
}
