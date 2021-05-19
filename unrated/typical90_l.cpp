#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

class Unionfind {
   public:
    ll N;
    vector<ll> parents;

    Unionfind(ll n0) {
        N = n0;
        parents = vector<ll>(N, -1);
    }

    ll find(ll x) {
        if (parents[x] < 0)
            return x;
        else {
            parents[x] = find(parents[x]);
            return parents[x];
        }
    }

    void unite(ll x, ll y) {
        x = find(x), y = find(y);
        if (x == y) return;
        if (parents[x] > parents[y]) {
            ll tmp = x;
            x = y, y = tmp;
        }
        parents[x] += parents[y];
        parents[y] = x;
    }

    bool same(ll x, ll y) { return (find(x) == find(y)); }
};

int main() {
    ll h, w, q;
    cin >> h >> w >> q;
    matll query(q, vector<ll>(5, 0));
    rep(i, q) {
        cin >> query[i][0];
        rep(j, query[i][0] * 2) cin >> query[i][j + 1];
    }

    vector<ll> grid(h * w, 0);
    Unionfind uf(h * w);
    for_itr(qi, query) {
        for_itr(qij, qi) qij -= 1;
        ll idx1 = qi[1] * w + qi[2];
        if (qi[0] == 0) {
            grid[idx1] = 1;
            if (qi[1] > 0 && grid[idx1 - w] == 1) uf.unite(idx1, idx1 - w);
            if (qi[1] + 1 < h && grid[idx1 + w] == 1) uf.unite(idx1, idx1 + w);
            if (qi[2] > 0 && grid[idx1 - 1] == 1) uf.unite(idx1, idx1 - 1);
            if (qi[2] + 1 < w && grid[idx1 + 1] == 1) uf.unite(idx1, idx1 + 1);
        } else if (qi[0] == 1) {
            ll idx2 = qi[3] * w + qi[4];
            bool res = uf.same(idx1, idx2);
            if (res && grid[idx1] == 1 && grid[idx2] == 1)
                cout << "Yes" << '\n';
            else
                cout << "No" << '\n';
        }
    }
    return 0;
}
