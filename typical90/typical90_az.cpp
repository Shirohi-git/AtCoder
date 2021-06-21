#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define sum(v) accumulate(v.begin(), v.end(), 0LL)

ll N;
matll A;
const ll MOD1 = 1e9 + 7;

int main() {
    cin >> N;
    A = matll(N, vecll(6));
    rep(i, N) rep(j, 6) cin >> A[i][j];

    ll ans = 1;
    repitr(ai, A) ans = ans * sum(ai) % MOD1;
    cout << ans << '\n';
    return 0;
}
