#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using tlll = tuple<ll, ll, ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

ll dfs(const vector<ll>& vec, ll p, ll q) {
    ll n = vec.size();
    vector<tlll> st(0);
    rep(i, n - 4) st.push_back(tlll(vec[i], i, 1));

    ll res = 0;
    ll mod, idx, cnt;
    while (!st.empty()) {
        tie(mod, idx, cnt) = st.back();
        st.pop_back();
        if (cnt == 5) {
            if (mod == q) res++;
            continue;
        }
        repr(j, idx + 1, n - 4 + cnt) {
            ll nxt = (mod * vec[j]) % p;
            st.push_back(tlll(nxt, j, cnt + 1));
        }
    }
    return res;
}

int main() {
    ll n, p, q;
    cin >> n >> p >> q;
    vector<ll> a(n);
    rep(i, n) cin >> a[i];

    ll ans = dfs(a, p, q);
    cout << ans << endl;
    return 0;
}
