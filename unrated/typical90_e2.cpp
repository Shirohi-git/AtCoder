#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

const ll MOD1 = 1e9 + 7;

// 小課題2 行列累乗 O(b3 logn)
int mat_product(matll a, matll b, matll& res) {
    ll n = a.size(), m = b.size(), l = b[0].size();
    rep(i, n) rep(j, l) rep(k, m) {
        res[i][j] += a[i][k] * b[k][j];
        res[i][j] %= MOD1;
    }
    return 0;
}

int mat_powlst(ll cnt, matll mat, vector<matll>& res) {
    res[0] = mat;
    rep(p, cnt) mat_product(res[p], res[p], res[p + 1]);
    return 0;
}

int main() {
    ll n, b, k;
    cin >> n >> b >> k;
    vector<ll> c(k);
    rep(i, k) { cin >> c[i]; }

    if (b > 30) return 0;
    const matll ZMAT(b, vector<ll>(b, 0));

    matll mat = ZMAT;
    rep(i, b) for_itr(cj, c) mat[i][(i * 10 + cj) % b] += 1;

    vector<matll> pow_lst(61, ZMAT);
    mat_powlst(60, mat, pow_lst);

    matll ans_mat = ZMAT;
    rep(i, b) ans_mat[i][i] = 1;
    rep(p, 60) {
        if ((n >> p) & 1) {
            matll tmp = ZMAT;
            mat_product(ans_mat, pow_lst[p], tmp);
            ans_mat = tmp;
        }
    }
    cout << ans_mat[0][0] << '\n';
    return 0;
}
