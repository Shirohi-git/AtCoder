#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define sort_all(v) (sort(v.begin(), v.end()))
#define all(v) (v).begin(), (v).end()

ll N, K;
vecll L;

int main() {
    cin >> N >> K;
    L = vecll(N);
    rep(i, N) cin >> L[i];

    sort_all(L), reverse(all(L));
    ll ans = 0;
    rep(i, K) ans += L[i];
    cout << ans << '\n';

    return 0;
}
