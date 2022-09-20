#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    matll cnt(26, vector<ll>(n + 1, 1e6));
    rep(i, n) cnt[s[i] - 'a'][i] = i;
    rep(i, 26) rep(tmp, n - 1) {
        ll j = n - 2 - tmp;
        if (cnt[i][j] == 1e6) cnt[i][j] = cnt[i][j + 1];
    }

    ll idx = 0;
    string ans = "";
    rep(j, k) rep(i, 26) {
        if (n - 1 - cnt[i][idx] >= k - 1 - j) {
            idx = cnt[i][idx] + 1;
            ans += s[idx - 1];
            break;
        }
    }
    cout << ans << endl;
    return 0;
}
