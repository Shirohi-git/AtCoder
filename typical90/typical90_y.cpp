#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

vecll ll_to_vec(ll num) {
    vecll res(0);
    while (num) {
        res.push_back(num % 10);
        num /= 10;
    }
    sort(res.begin(), res.end());
    return res;
}

matll cmb_multi(ll n, ll r) {
    matll now(n - 1, vecll(0));
    rep(i, n - 1) now[i].push_back(i + 1);

    matll res = now;
    rep(i, r - 1) {
        matll nxt(0, vecll(0));
        repitr(cmb, now) {
            ll num = cmb.back(), last = cmb.size();
            cmb.push_back(num);
            repr(j, num, n) {
                cmb[last] = j;
                nxt.push_back(cmb), res.push_back(cmb);
            }
        }
        now = nxt;
    }
    return res;
}

int main() {
    ll n, b;
    cin >> n >> b;

    ll ans = 0;
    repitr(cmb, cmb_multi(10, 11)) {
        ll num = 1;
        repitr(i, cmb) num *= i;
        if (b + num <= n && cmb == ll_to_vec(b + num)) ans++;
    }
    if (b <= n && ll_to_vec(b)[0] == 0) ans++;
    cout << ans << endl;
    return 0;
}
