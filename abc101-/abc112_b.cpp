#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))

ll N, T;
matll CT;

int main() {
    cin >> N >> T;
    CT = matll(N, vecll(2, 0));
    rep(i, N) cin >> CT[i][0] >> CT[i][1];

    ll ans = 10000;
    repitr(cti, CT) if (cti[1] <= T) ans = min(ans, cti[0]);

    if (ans == 10000)
        cout << "TLE" << '\n';
    else
        cout << ans << '\n';

    return 0;
}
