#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N, T, A;
vecll H;
const ll INF = 100000000;

int main() {
    cin >> N >> T >> A;
    H = vecll(N);
    rep(i, N) cin >> H[i];
    A *= 1000, T *= 1000;

    ll ans = 1, val = INF;
    rep(i, N) if (val > abs(A - (T - H[i] * 6))) {
        ans = i + 1;
        val = abs(A - (T - H[i] * 6));
    }
    cout << ans << '\n';
    return 0;
}
