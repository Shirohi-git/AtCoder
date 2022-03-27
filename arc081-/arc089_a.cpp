#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N;
matll TXY;

int main() {
    cin >> N;
    TXY = matll(N, vecll(3, 0));
    rep(i, N) rep(j, 3) cin >> TXY[i][j];

    string ans = "Yes";
    vecll bfo = {0, 0, 0};
    repitr(txy, TXY) {
        ll t = txy[0] - bfo[0];
        ll x = abs(txy[1] - bfo[1]), y = abs(txy[2] - bfo[2]);
        if (x + y > t) ans = "No";
        if ((t - x - y) % 2 == 1) ans = "No";
        bfo = txy;
    }

    cout << ans << '\n';
    return 0;
}
