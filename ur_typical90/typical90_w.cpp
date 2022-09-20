#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)

const ll MOD1 = 1e9 + 7;

tuple<ll, vecll, vecll> make_dict(ll w) {
    vecll stack = {0, 1};
    rep(i, w + 2) {
        ll bfo = 1 << i, now = 1 << (i + 1);
        vecll tmp(0);
        repitr(num, stack) if ((bfo & num) == 0) tmp.push_back(now + num);
        stack.insert(stack.end(), tmp.begin(), tmp.end());
    }
    ll large = stack.back();
    vecll res(large + 1, -1);
    rep(i, stack.size()) res[stack[i]] = i;
    return make_tuple(stack.size(), res, stack);
}

int main() {
    ll h, w;
    cin >> h >> w;
    vector<string> c(h + 1);
    c[0] = string(w + 2, '#');
    rep(i, h) {
        cin >> c[i + 1];
        c[i + 1] = '#' + c[i + 1] + '#';
    }

    ll dp_size;
    vecll dict, rvdict;
    tie(dp_size, dict, rvdict) = make_dict(w);

    const ll pow2w = 1 << (w + 2);
    const ll judge = pow2w + 7;
    vecll nowdp(dp_size, 0), nxtdp(dp_size, 0);
    nowdp[0] = 1;

    rep(i, h + 1) rep(j, w + 2) {
        nxtdp = vecll(dp_size, 0);
        rep(k, dp_size) {
            ll bit = rvdict[k], cnt = nowdp[k];
            ll nxt0 = dict[bit >> 1];
            nxtdp[nxt0] += cnt;
            if (nxtdp[nxt0] > MOD1) nxtdp[nxt0] -= MOD1;
            if ((c[i][j] == '.') && ((bit & judge) == 0)) {
                ll nxt1 = dict[(bit >> 1) + pow2w];
                nxtdp[nxt1] += cnt;
                if (nxtdp[nxt1] > MOD1) nxtdp[nxt1] -= MOD1;
                continue;
            }
        }
        nowdp = nxtdp;
    }

    ll ans = 0;
    repitr(cnt, nowdp) {
        ans += cnt;
        if (ans > MOD1) ans -= MOD1;
    }
    cout << ans << endl;
    return 0;
}
