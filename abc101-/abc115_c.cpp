#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define sort_all(v) (sort(v.begin(), v.end()))

ll N, K;
vecll H;

int main() {
    cin >> N >> K;
    H = vecll(N);
    rep(i, N) cin >> H[i];
    sort_all(H);

    ll ans = 1000000000;
    rep(i, N-K+1) ans = min(H[i+K-1] - H[i], ans);
    cout << ans << '\n';

    return 0;
}
