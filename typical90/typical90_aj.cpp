#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define max_val(v) *max_element(v.begin(), v.end())

ll N, Q;
matll XY;
vecll QUERY;

int main() {
    cin >> N >> Q;
    XY = matll(N, vecll(2));
    rep(i, N) cin >> XY[i][0] >> XY[i][1];
    QUERY = vecll(Q);
    rep(i, Q) cin >> QUERY[i];

    ll pp = -1e10, pm = -1e10, mp = -1e10, mm = -1e10;
    repitr(xy, XY) {
        ll x = xy[0], y = xy[1];
        pp = max(pp, x + y), pm = max(pm, x - y);
        mp = max(mp, -x + y), mm = max(mm, -x - y);
    }
    repitr(i, QUERY) {
        ll x = XY[i - 1][0], y = XY[i - 1][1];
        vecll tmp = {pp - x - y, pm - x + y, mp + x - y, mm + x + y};
        cout << max_val(tmp) << '\n';
    }
    return 0;
}
