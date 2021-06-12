#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)
#define reprms(i, a, b, s) for (ll i = ll(a); i > ll(b); i += s)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)
#define sort_all(v) sort(v.begin(), v.end())
#define min_val(v) *min_element(v.begin(), v.end())
#define max_val(v) *max_element(v.begin(), v.end())
#define max_idx(v) distance(v.begin(), max_element(v.begin(), v.end()))
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define all(v) v.begin(), v.end()
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

// is all true?
bool f_all(const vecll vec0, const vecll vec1) {
    ll n = vec0.size();
    rep(i, n) if (vec0[i] != vec1[i]) return false;
    return true;
}

// 数値桁分け
vecll ll_to_vec(ll num) {
    vecll res(0);
    while (num) {
        res.push_back(num % 10);
        num /= 10;
    }
    return res;
}

// counter
vecll counter(const vecll& vec0, ll max_v) {
    vecll res(max_v + 1, 0);
    repitr(num, vec0) res[num]++;
    return res;
}

// 累乗
ll f_pow(ll x, ll y) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res *= x;
        x *= x, y >>= 1;
    }
    return res;
}

// 累乗(mod)
ll mod_pow(ll x, ll y, const ll& mod) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x) % mod;
        x = (x * x) % mod;
        y >>= 1;
    }
    return res;
}

// 組合せ no_mul = 0(重複有), = 1(重複無)
matll combi_itr(const ll& no_mul, const vecll& vec0, ll r) {
    ll n = vec0.size();
    matll now(n, vecll(0));
    rep(i, n) now[i].push_back(i);
    rep(i, r - 1) {
        matll nxt(0, vecll(0));
        repitr(com, now) {
            ll num = com.back(), last = com.size();
            com.push_back(num);
            repr(j, num + no_mul, n) {
                com[last] = j;
                nxt.push_back(com);
            }
        }
        now = nxt;
    }
    repitr(comi, now) repitr(idx, comi) idx = vec0[idx];
    return now;
}

int main() {
    ll n;
    cin >> n;

    return 0;
}
