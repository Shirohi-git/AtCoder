#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))

ll N;
vecll A;

int main() {
    cin >> N;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll ans = 0;
    repitr(ai, A) while (ai % 2 == 0) ans += 1, ai /= 2;
    cout << ans << '\n';
    return 0;
}
