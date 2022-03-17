#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, H, W;
matll AB;

int main() {
    cin >> N >> H >> W;
    AB = matll(N, vecll(2, 0));
    rep(i, N) cin >> AB[i][0] >> AB[i][1];

    ll ans = 0;
    repitr(ab, AB) if (ab[0] >= H && ab[1] >= W) ans += 1;
    cout << ans << '\n';

    return 0;
}
