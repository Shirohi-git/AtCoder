#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

//小課題1 O(m2)
int main() {
    ll n, m;
    cin >> n >> m;
    matll lr(m, vector<ll>(2, -1));
    rep(i, m) cin >> lr[i][0] >> lr[i][1];

    if (m > 1000) return 0;
    ll ans = 0;
    for_itr(lri, lr) for_itr(lrj, lr) {
        if (lri[0] < lrj[0] && lrj[0] < lri[1] && lri[1] < lrj[1]) ans++;
    }
    cout << ans << endl;
    return 0;
}
