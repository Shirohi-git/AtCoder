#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N, S;
matll AB;

int main() {
    cin >> N >> S;
    AB = matll(N, vecll(2));
    rep(i, N) cin >> AB[i][0] >> AB[i][1];

    matll dp(N + 1, vecll(S + 2, 0));
    dp[0][0] = 1;
    rep(i, N) rep(j, S) {
        ll a = AB[i][0], b = AB[i][1];
        dp[i + 1][min(S + 1, j + a)] |= dp[i][j];
        dp[i + 1][min(S + 1, j + b)] |= dp[i][j];
    }

    if (!dp[N][S]) {
        cout << "Impossible" << '\n';
        return 0;
    }

    ll now = S;
    string ans = "";
    rep(j, N) {
        ll i = N - j;
        ll a = AB[i - 1][0], b = AB[i - 1][1];
        if (now >= a && dp[i - 1][now - a])
            now -= a, ans += 'A';
        else if (now >= b && dp[i - 1][now - b])
            now -= b, ans += 'B';
    }
    reverse(ans.begin(), ans.end());
    cout << ans << '\n';
    return 0;
}
