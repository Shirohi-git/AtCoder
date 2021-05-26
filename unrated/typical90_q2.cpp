#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

//小課題2 O(n2)
int main() {
    ll n, m;
    cin >> n >> m;
    matll lr(m, vector<ll>(2, -1));
    rep(i, m) cin >> lr[i][0] >> lr[i][1];

    if (n > 1000) return 0;
    matll out(n, vector<ll>(n, 0));
    for_itr(lri, lr) out[lri[0] - 1][lri[1] - 1]++;

    ll ans = 0;
    vector<ll> vec(n, 0);
    rep(i, n) {
        ll sumout = sum(out[i]);
        vec[i] = 0;
        rep(j, n) {
            sumout -= out[i][j];
            ans += sumout * vec[j];
            vec[j] += out[i][j];
        }
    }
    cout << ans << endl;
    return 0;
}
