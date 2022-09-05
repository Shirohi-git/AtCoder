#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define all(v) v.begin(), v.end()

ll N;
matll XY;

int main() {
    cin >> N;
    XY = matll(N, vecll(2));
    rep(i, N) cin >> XY[i][0] >> XY[i][1];

    vecll idx(N, 0), res(0);
    rep(i, N) idx[i] = i;
    rep(i, 2) {
        sort(all(idx), [=](ll& x, ll& y) { return XY[x][i] < XY[y][i]; });
        vecll tmp{idx[0], idx[1], idx[N - 1], idx[N - 2]};
        repitr(v, tmp) if (find(all(res), v) == res.end()) res.push_back(v);
    }

    vecll ans(0);
    rep(p, res.size()) repr(q, p + 1, res.size()) {
        vecll XYi = XY[res[p]], XYj = XY[res[q]];
        ll dist = max(abs(XYj[0] - XYi[0]), abs(XYj[1] - XYi[1]));
        ans.push_back(dist);
    }
    sort(all(ans), std::greater<int>());
    cout << ans[1] << '\n';
    return 0;
}
