#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define max_val(v) (*max_element(v.begin(), v.end()))
#define sum(v) (accumulate(v.begin(), v.end(), 0LL))

ll N;
vecll P;

int main() {
    cin >> N;
    P = vecll(N);
    rep(i, N) cin >> P[i];

    ll ans = sum(P) - max_val(P) / 2;
    cout << ans << '\n';
    return 0;
}
