#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define min_val(v) (*min_element((v).begin(), (v).end()))
#define max_val(v) (*max_element((v).begin(), (v).end()))

ll N, M, X, Y;
vecll VX, VY;

int main() {
    cin >> N >> M;
    VX = vecll(N+1), VY = vecll(M+1);
    cin >> VX[0] >> VY[0];
    rep(i, N) cin >> VX[i+1];
    rep(i, M) cin >> VY[i+1];

    ll zx = max_val(VX), zy = min_val(VY);
    str ans = "War";
    if (zx < zy) ans = "No War";
    cout << ans << '\n';
    return 0;
}
