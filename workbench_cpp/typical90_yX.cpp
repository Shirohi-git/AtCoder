#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

ll f_pow(ll x, ll y) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res *= x;
        x *= x, y >>= 1;
    }
    return res;
}

bool f_all(const vecll vec0, const vecll vec1) {
    ll n = vec0.size();
    repr(i, 1, n) if (vec0[i] != vec1[i]) return false;
    return true;
}

vecll ll_to_vec(ll num) {
    vecll res(0);
    while (num) {
        res.push_back(num % 10);
        num /= 10;
    }
    return res;
}

vecll counter(const vecll& vec0) {
    vecll res(10, 0);
    repitr(num, vec0) res[num]++;
    return res;
}

matll cmb_multi(const vecll& vec0, ll r) {
    ll n = vec0.size();
    matll now(n, vecll(0));
    rep(i, n) now[i].push_back(i);

    rep(i, r - 1) {
        matll nxt(0, vecll(0));
        repitr(com, now) {
            ll num = com.back(), last = com.size();
            com.push_back(num);
            repr(j, num, n) {
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
    ll n, b;
    cin >> n >> b;

    vecll numvec(10, 0);
    rep(i, 10) numvec[i] = i;
    matll cmb_mul = cmb_multi(numvec, 10);

    ll ans = 0;
    vecll b0_cnt = counter(ll_to_vec(b));
    repitr(cmb, cmb_mul) {
        vecll cnt = counter(cmb);
        ll num = 1;
        repr(i, 1, 10) num *= f_pow(i, cnt[i]);
        vecll b_cnt = counter(ll_to_vec(b + num));
        if (b + num <= n && b_cnt[0] == 0 && f_all(cnt, b_cnt)) ans++;
        if (b <= n && b0_cnt[0] > 0 && f_all(cnt, b0_cnt)) ans++;
    }
    cout << ans << endl;
    return 0;
}
