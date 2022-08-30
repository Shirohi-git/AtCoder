#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define min_val(v) (*min_element((v).begin(), (v).end()))
#define sum(v) (accumulate((v).begin(), (v).end(), 0LL))

ll N, X;
vecll M;

int main() {
    cin >> N >> X;
    M = vecll(N);
    rep(i, N) cin >> M[i];

    ll x = X - sum(M), ans = N;
    ans += x / min_val(M);
    cout << ans << '\n';
    return 0;
}
