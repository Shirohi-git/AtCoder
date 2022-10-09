#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))

ll N;
matll LR;

int main() {
    cin >> N;
    LR = matll(N, vecll(2, 0));
    rep(i, N) cin >> LR[i][0] >> LR[i][1];

    ll ans = 0;
    repitr(lr, LR) ans += lr[1] - lr[0] + 1;
    cout << ans << '\n';
    return 0;
}
