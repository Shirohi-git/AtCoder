#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

class Fenwicktree {
   private:
    vector<ll> tree;

   public:
    ll N;
    Fenwicktree(int n0) {
        N = n0;
        tree = vector<ll>(N, 0);
    }

    ll accsum(int r) {
        ll res = 0;
        r++;
        while (r > 0) {
            res += tree[r - 1];
            r -= r & -r;
        }
        return res;
    }

    void update(ll idx, ll x) {
        idx++;
        while (idx <= N) {
            tree[idx - 1] += x;
            idx += idx & -idx;
        }
        return;
    }

    ll query(ll l, ll r) { return accsum(r - 1) - accsum(l - 1); }
};

int main() {
    ll n, m;
    cin >> n >> m;
    matll lr(m, vector<ll>(2, -1));
    rep(i, m) {
        cin >> lr[i][0] >> lr[i][1];
        lr[i][0]--, lr[i][1]--;
        lr[i][1] *= -1;
    }
    sort_all(lr);

    Fenwicktree bit(n);
    ll ans = 0;
    for_itr(lri, lr) {
        ll l = lri[0], r = -lri[1];
        bit.update(r, 1);
        ans += bit.query(l + 1, r);
    }
    cout << ans << endl;
    return 0;
}
