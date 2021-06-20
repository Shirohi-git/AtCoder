#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)


ll N, L;
const ll MOD1 = 1e9 + 7;

int main() {
    cin >> N >> L;

    vecll dp(N + L + 1, 0);
    dp[0] = 1;
    rep(i, N + 1) {
        if (dp[i] >= MOD1) dp[i] -= MOD1;
        dp[i + 1] += dp[i];
        dp[i + L] += dp[i];
    }
    cout << dp[N] << '\n';
    return 0;
}
