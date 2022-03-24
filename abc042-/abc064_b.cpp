#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define min_val(v) (*min_element(v.begin(), v.end()))
#define max_val(v) (*max_element(v.begin(), v.end()))

ll N;
vecll A;

int main() {
    cin >> N;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll ans = max_val(A) - min_val(A);
    cout << ans << '\n';

    return 0;
}
