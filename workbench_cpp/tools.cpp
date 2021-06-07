#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define min_val(v) *min_element(v.begin(), v.end())
#define max_val(v) *max_element(v.begin(), v.end())
#define max_idx(v) distance(v.begin(), max_element(v.begin(), v.end()))
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

// 二分探索判定
bool isOK(ll mid) {
    bool res;
    if (res)
        return true;
    else
        return false;
}

// 二分探索
ll binary_search(ll l, ll r) {
    ll left = l, right = r + 1;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (isOK(mid))
            right = mid;
        else
            left = mid;
    }
    return left;
}

// 組合せ数
class Combination {
   private:
    vector<ll> fact, inv, factinv;

    ll mod_pow(ll x, ll y, const ll& mod) {
        ll res = 1;
        while (y > 0) {
            if (y & 1) res = (res * x) % mod;
            x = (x * x) % mod;
            y >>= 1;
        }
        return res;
    }

   public:
    ll N, MOD;

    Combination(ll n0, ll mod) {
        N = n0, MOD = mod;
        fact = vector<ll>(N + 1, -1);
        inv = vector<ll>(N + 1, -1);
        factinv = vector<ll>(N + 1, -1);

        fact[0] = 1, fact[1] = 1;
        inv[0] = 0, inv[1] = 1;
        factinv[0] = 1, factinv[1] = 1;
        repr(i, 2, N + 1) {
            fact[i] = (fact[i - 1] * i) % MOD;
            inv[i] = mod_pow(i, MOD - 2, MOD);
            factinv[i] = (factinv[i - 1] * inv[i]) % MOD;
        }
    }

    ll count(ll cn, ll cr) {
        if ((cr < 0) || (cn < cr)) return 0;
        cr = min(cr, cn - cr);
        ll res = fact[cn] * factinv[cr] % MOD;
        res = res * factinv[cn - cr] % MOD;
        return (res % MOD + MOD) % MOD;
    }
};

// Fenwicktree(BinaryIndexedTree) 0-indexed
class Fenwicktree {
   private:
    vector<ll> tree;

   public:
    ll N;
    Fenwicktree(int n0) {
        N = n0;
        tree = vector<ll>(N, 0);
    }

    // RSQ[0,r]
    ll accsum(int r) {
        ll res = 0;
        r++;
        while (r > 0) {
            res += tree[r - 1];
            r -= r & -r;
        }
        return res;
    }

    // update vec[idx] += x
    void update(ll idx, ll x) {
        idx++;
        while (idx <= N) {
            tree[idx - 1] += x;
            idx += idx & -idx;
        }
        return;
    }

    // RSQ[l,r)
    ll query(ll l, ll r) { return accsum(r - 1) - accsum(l - 1); }
};

// 遅延Segtree RMQ and (RUQ or RAQ)
class LazySegtree {
   private:
    // 区間にしたい操作 ex) max, min
    ll segfunc(ll x, ll y) { return max(x, y); }

    // RUQ or RAQ
    void ruq_or_raq(ll k, ll x) {
        if (lazy[k].empty()) lazy[k].push_back(0);
        // RUQ
        lazy[k][0] = x, data[k] = x;
        // RAQ
        // lazy[k][0] += x, data[k] += x;
        return;
    }

    ll bit_length(ll x) {
        ll cnt = 0;
        while (x) cnt++, x >>= 1;
        return cnt;
    }

    // 伝搬する対象の区間, 伝搬する必要のある最大の左閉区間 lm と右閉区間 rm
    vecll gindex(ll l, ll r) {
        l += num, r += num;
        ll lm = l >> bit_length(l & (~l + 1));
        ll rm = r >> bit_length(r & (~r + 1));

        vecll idx(0);
        while (r > l) {
            if (l <= lm) idx.push_back(l);
            if (r <= rm) idx.push_back(r);
            l >>= 1, r >>= 1;
        }
        while (l) {
            idx.push_back(l);
            l >>= 1;
        }
        return idx;
    }

    // 遅延伝搬処理 ids: 伝搬する対象の区間
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

    // ini: 配列の初期値, ele: 単位元, 遅延初期化注意
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

    // 区間[l, r)の値をxに更新
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

    // [l, r)のsegfuncしたものを得る
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

// 行列積
int mat_product(matll a, matll b, matll& res) {
    ll n = a.size(), m = b.size(), l = b[0].size();
    if (m != a[0].size()) {
        cout << "can't\n";
        return 0;
    }
    rep(i, n) rep(j, l) rep(k, m) { res[i][j] += a[i][k] * b[k][j]; }
    return 0;
}

// 行列累乗 res[i] = mat**(2**i)
int mat_powlst(ll cnt, matll mat, vector<matll>& res) {
    res[0] = mat;
    rep(p, cnt) mat_product(res[p], res[p], res[p + 1]);
    return 0;
}

int main() {
    ll n;
    cin >> n;

    return 0;
}
