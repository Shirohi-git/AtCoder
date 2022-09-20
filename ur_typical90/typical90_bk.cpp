#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)


bool f_all(const vecll vec0, const ll num) {
    ll n = vec0.size();
    rep(i, n) if (vec0[i] != num) return false;
    return true;
}

matll combi_itr(const ll &no_mul, const ll& n, ll r) {
    matll now(n, vecll(0)), res(0);
    rep(i, n) now[i].push_back(i);

    res = now;
    rep(i, r - 1) {
        matll nxt(0, vecll(0));
        repitr(com, now) {
            ll num = com.back(), last = com.size();
            com.push_back(num);
            repr(j, num + no_mul, n) {
                com[last] = j;
                nxt.push_back(com), res.push_back(com);
            }
        }
        now = nxt;
    }
    return res;
}

int main() {
    ll h, w;
    cin >> h >> w;
    matll p(h, vecll(w, 0));
    rep(i, h) rep(j, w) cin >> p[i][j];

    ll ans = 0;
    repitr(cmb, combi_itr(1, h, h)) {
        map<ll, ll> cnt;
        rep(j, w) {
            ll num = p[cmb[0]][j];
            vecll tmp(0);
            repitr(i, cmb) tmp.push_back(p[i][j]);
            if (f_all(tmp, num)) cnt[num]++;
        }
        ll max_cnt = 0;
        repdic(_, v, cnt) max_cnt = max(max_cnt, v);
        ans = max(ans, max_cnt * ll(cmb.size()));
    }
    cout << ans << endl;
    return 0;
}
