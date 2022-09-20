#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define reprms(i, a, b, s) for (ll i = ll(a); i > ll(b); i += s)

class Segtree {
   private:
    ll bit_length(ll x) {
        ll cnt = 0;
        while (x) cnt++, x >>= 1;
        return cnt;
    }

   public:
    ll ide_ele, num;
    vecll tree;

    Segtree(const ll& n0, const ll ele0) {
        ide_ele = ele0, num = 1 << bit_length(n0 - 1);
        tree = vecll(2 * num, ele0);
    }

    ll query(ll l, ll r) {
        ll res = ide_ele;
        l += num, r += num;
        while (l < r) {
            if (l & 1) {
                res = max(res, tree[l]);
                l++;
            }
            if (r & 1) res = max(res, tree[r - 1]);
            l >>= 1, r >>= 1;
        }
        return res;
    }

    ll getval(ll k) { return tree[num + k]; }

    void point_update(ll k, ll x) {
        tree[num + k] = x;
        return;
    }

    void all_update(void) {
        reprms(i, num - 1, 0, -1) {
            tree[i] = max(tree[i * 2], tree[i * 2 + 1]);
        }
        return;
    }
};

const ll MININF = -(1LL << 31);
ll W, N;
matll LRV;

int main() {
    cin >> W >> N;
    LRV = matll(N, vecll(3, 0));
    rep(i, N) rep(j, 3) cin >> LRV[i][j];

    Segtree seg(W+1, MININF);
    seg.point_update(0, 0LL);
    repitr(lrv, LRV) {
        seg.all_update();
        ll l = lrv[0], r = lrv[1], v = lrv[2];
        reprms(j, W, l - 1, -1) {
            ll tmp = seg.query(max(0LL, j - r), j - l + 1);
            if (tmp + v > max(seg.getval(j), 0LL)) seg.point_update(j, tmp + v);
        }
    }
    ll ans = seg.getval(W);
    if (ans <= 0) ans = -1;
    cout << ans << endl;
    return 0;
}
