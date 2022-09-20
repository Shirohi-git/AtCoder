#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

class LazySegtree {
   private:
    ll segfunc(ll x, ll y) { return max(x, y); }

    void ruq_or_raq(ll k, ll x) {
        if (lazy[k].empty()) lazy[k].push_back(0);
        lazy[k][0] = x, data[k] = x;
        return;
    }

    ll bit_length(ll x) {
        ll cnt = 0;
        while (x) cnt++, x >>= 1;
        return cnt;
    }

    vecll gindex(ll l, ll r) {
        l += num, r += num;
        ll lm = l >> bit_length(l & (~l + 1));
        ll rm = r >> bit_length(r & (~r + 1));

        vecll idx(0);
        while (r > l) {
            if (l <= lm) idx.push_back(l);
            if (r <= rm) idx.push_back(r);
            r >>= 1, l >>= 1;
        }
        while (l) {
            idx.push_back(l);
            l >>= 1;
        }
        return idx;
    }

    void propagates(vecll ids) {
        reverse(all(ids));
        repitr(i, ids) {
            if (lazy[i].empty()) continue;
            ll v = lazy[i].back();
            lazy[i].pop_back();
            ruq_or_raq(2 * i, v);
            ruq_or_raq(2 * i + 1, v);
        }
        return;
    }

   public:
    ll ele, num;
    vecll data;
    matll lazy;

    LazySegtree(vecll ini, ll ele0) {
        ll n = ini.size();
        ele = ele0;
        num = 1 << bit_length(n - 1);
        data = vecll(num * 2, ele);
        lazy = matll(num * 2, vecll(0));
        rep(i, n) data[num + i] = ini[i];
        for (ll i = num - 1; i > 0; i--)
            data[i] = segfunc(data[i * 2], data[i * 2 + 1]);
    }

    void update(ll l, ll r, ll x) {
        vecll ids = gindex(l, r);
        propagates(ids);

        l += num, r += num;
        while (l < r) {
            if (l & 1) ruq_or_raq(l, x), l++;
            if (r & 1) ruq_or_raq(r - 1, x);
            l >>= 1, r >>= 1;
        }
        repitr(i, ids) data[i] = segfunc(data[i * 2], data[i * 2 + 1]);
        return;
    }

    ll query(ll l, ll r) {
        vecll ids = gindex(l, r);
        propagates(ids);

        ll res = ele;
        l += num, r += num;
        while (l < r) {
            if (l & 1) res = segfunc(res, data[l]), l++;
            if (r & 1) res = segfunc(res, data[r - 1]);
            l >>= 1, r >>= 1;
        }
        return res;
    }
};

int main() {
    ll w, n;
    cin >> w >> n;
    matll lr(n, vecll(2, 0));
    rep(i, n) cin >> lr[i][0] >> lr[i][1];

    LazySegtree lseg(vecll(w, 0), 0);
    repitr(lri, lr) {
        ll ans = lseg.query(lri[0] - 1, lri[1]) + 1;
        lseg.update(lri[0] - 1, lri[1], ans);
        cout << ans << '\n';
    }
    return 0;
}
