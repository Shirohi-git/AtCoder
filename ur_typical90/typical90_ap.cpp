#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

const ll MOD1 = 1e9 + 7;
ll K;

int main() {
    cin >> K;
    if (K % 9) {
        cout << 0 << endl;
        return 0;
    }

    vecll dp(K + 1, 0);
    dp[0] = 1;
    rep(i, K) repr(j, 1, 10) {
        if (i + j > K) break;
        dp[i + j] += dp[i];
        if (dp[i + j] >= MOD1) dp[i + j] -= MOD1;
    }
    cout << dp[K] << endl;
    return 0;
}
