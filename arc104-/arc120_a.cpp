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

    ll a_max = 0, ans = 0, a_sum = 0;
    rep(i, N) {
        a_max = max(A[i], a_max);
        a_sum += A[i];
        ans += a_sum;
        cout << ans + (i + 1) * a_max << '\n';
    }

    return 0;
}
