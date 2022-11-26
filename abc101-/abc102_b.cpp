#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N;
vecll A;

int main() {
    cin >> N;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll ans = 0;
    rep(i, N) rep(j, i) ans = max(ans, abs(A[i] - A[j]));
    cout << ans << '\n';
    return 0;
}
